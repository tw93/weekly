from python_graphql_client import GraphqlClient
import feedparser
import httpx
import json
import pathlib
import re
import os
import datetime

root = pathlib.Path(__file__).parent.resolve()
client = GraphqlClient(endpoint="https://api.github.com/graphql")

TOKEN = os.environ.get("GH_TOKEN", "")

def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)

def formatGMTime(timestamp):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    dateStr = datetime.datetime.strptime(timestamp, GMT_FORMAT) + datetime.timedelta(hours=8)
    return dateStr.date()

def repository_get():
    return """
      repository(owner: 'tw93',name: 'weekly') {
          object(expression: "master:md/") {
            ... on Tree {
              entries {
                name
                type
                mode
                object {
                  ... on Blob {
                    byteSize
                    text
                    isBinary
                  }
                }
              }
            }
          }
      }
    """


def fetch_files(oauth_token):
    data = client.execute(
      query = repository_get(),
      headers={"Authorization": "Bearer {}".format(oauth_token)},
    )
    print()
    print(">>>>>>>here\n")
    print(data)
    print(json.dumps(data, indent=4))
    print()
    return data

if __name__ == "__main__":
    readme = root / "README.md"
    releases = fetch_files(TOKEN)
    md = "\nhello,world"
    readme_contents = readme.open().read()
    rewritten = replace_chunk(readme_contents, "recent_releases", md)
    readme.open("w").write(rewritten)

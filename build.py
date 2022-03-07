import os
import time
import httpx
import urllib.parse

def fetch_ci_time(filePath):
    entries = httpx.get("https://api.github.com/repos/tw93/weekly/commits?path=" + filePath + "&page=1&per_page=1")
    print(entries.json())
    return 1
    # return time.strptime(entries.json()[0].commit.committer.date,"%Y-%m-%d")


if __name__ == "__main__":
  readmefile=open('README.md','w')
  readmefile.write("# 潮流前端周刊\n")
  recentfile=open('RECENT.md','w')

  for root, dirs, filenames in os.walk('./md'):
    filenames.sort(reverse=True)

  for index, name in enumerate(filenames):
      if name.endswith('.md'):
        filepath = "/md/" + urllib.parse.quote(name)
        url   = 'https://github.com/tw93/weekly/tree/main' + filepath
        modified = fetch_ci_time(filepath)
        title = name.split('.md')[0]
        # recentMd= '* [{}]({}) - {}\n'.format(title, url, modified)
        readmeMd= '* [{}]({})\n'.format(title, url)
        if index < 6 :
          recentfile.write(readmeMd)
        readmefile.write(readmeMd)

  recentfile.close()
  readmefile.close()

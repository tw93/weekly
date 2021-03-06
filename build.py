import os
import httpx
import urllib.parse
import datetime

def fetch_ci_time(filePath):
    entries = httpx.get("https://api.github.com/repos/tw93/weekly/commits?path=" + filePath + "&page=1&per_page=1")
    ciTime= entries.json()[0]["commit"]["committer"]["date"].split("T")[0]
    return ciTime
    # return datetime.datetime.strptime(ciTime,"%Y-%m-%d")

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
        title = name.split('.md')[0]
        readmeMd= '* [{}]({})\n'.format(title, url)
        if index < 5 :
          modified = fetch_ci_time(filepath)
          recentMd= '* [{}]({}) - {}\n'.format(title, url, modified)
          recentfile.write(recentMd)
        readmefile.write(readmeMd)

  recentfile.close()
  readmefile.close()

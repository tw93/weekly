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
  readmefile.write("# 潮流周刊\n> 🩴 记录工程师 Tw93 的不枯燥生活，每周一发布\n")
  recentfile=open('RECENT.md','w')

  for root, dirs, filenames in os.walk('./src/pages/posts'):
    filenames.sort(reverse=True)

  for index, name in enumerate(filenames):
      if name.endswith('.md'):
        filepath = urllib.parse.quote(name)
        url   = 'http://weekly.tw93.fun/' + filepath
        oldTitle = name.split('.md')[0]
        title = '第' + oldTitle.split('-')[0] + '期 - ' + oldTitle.split('-')[1];
        readmeMd= '* [{}]({})\n'.format(title, url)
        if index < 5 :
          modified = fetch_ci_time("/src/pages/posts/"+filepath)
          recentMd= '* [{}]({}) - {}\n'.format(title, url, modified)
          recentfile.write(recentMd)
        readmefile.write(readmeMd)

  recentfile.close()
  readmefile.close()

import os
import httpx
import re
import urllib.parse
import datetime

def fetch_ci_time(filePath):
    entries = httpx.get("https://api.github.com/repos/tw93/weekly/commits?path=" + filePath + "&page=1&per_page=1")
    ciTime= entries.json()[0]["commit"]["committer"]["date"].split("T")[0]
    return ciTime
    # return datetime.datetime.strptime(ciTime,"%Y-%m-%d")

if __name__ == "__main__":
  readmefile=open('README.md','w')
  readmefile.write("# 潮流周刊\n\n> 记录工程师 Tw93 的不枯燥生活，欢迎订阅，也欢迎 [推荐](https://github.com/tw93/weekly/discussions/22) 你的好东西，Fork 自用可见 [开发文档](https://github.com/tw93/weekly/blob/main/Deploy.md)，期待你玩得开心~\n\n")
  recentfile=open('RECENT.md','w')

  for root, dirs, filenames in os.walk('./src/pages/posts'):
    filenames = sorted(filenames, key=lambda x:float(re.findall("(\d+)",x)[0]), reverse=True)

  for index, name in enumerate(filenames):
      if name.endswith('.md'):
        filepath = urllib.parse.quote(name)
        oldTitle = name.split('.md')[0]
        url   = 'https://weekly.tw93.fun/posts/' + oldTitle
        title = '第 ' + oldTitle.split('-')[0] + ' 期 - ' + oldTitle.split('-')[1]
        readmeMd= '* [{}]({})\n'.format(title, url)
        dateList = ["2022-10-10","2022-09-26","2022-09-12","2022-09-05","2022-08-29"]
        num = int(oldTitle.split('-')[0])
        if index < 5 :
          if num < 100 :
            modified = dateList[99-num]
          else :
            modified = fetch_ci_time('/src/pages/posts/' + filepath)

          recentMd= '* [{}]({}) - {}\n'.format(title, url, modified)
          recentfile.write(recentMd)
        readmefile.write(readmeMd)

  recentfile.close()
  readmefile.close()

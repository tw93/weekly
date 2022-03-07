import os
import datetime
import time
import urllib.parse

def formatTime(timestamp):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

if __name__ == "__main__":
  readmefile=open('README.md','w')
  readmefile.write("# 潮流前端周刊\n")
  recentfile=open('RECENT.md','w')

  for root, dirs, filenames in os.walk('./md'):
    filenames.sort(reverse=True)

  for index, name in enumerate(filenames):
      if name.endswith('.md'):
        filepath   = 'https://github.com/tw93/weekly/tree/main/md/' + urllib.parse.quote(name)
        modified = time.ctime(os.path.getmtime('md/'+name))
        print(modified)
        title = name.split('.md')[0]
        # recentMd= '* [{}]({}) - {}\n'.format(title, filepath, modified)
        readmeMd= '* [{}]({})\n'.format(title, filepath)
        if index < 6 :
          recentfile.write(readmeMd)
        readmefile.write(readmeMd)

  recentfile.close()
  readmefile.close()

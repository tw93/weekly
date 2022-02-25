import os
import datetime
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
        print(os.path.getctime('md/'+name))
        modified = formatTime(os.path.getctime('md/'+name))
        title = name.split('.md')[0]
        recentMd= '* [{}]({}) - {}\n'.format(title, filepath, modified)
        readmeMd= '* [{}]({})\n'.format(title, filepath, modified)
        if index < 6 :
          recentfile.write(recentMd)
        readmefile.write(readmeMd)

  recentfile.close()
  readmefile.close()

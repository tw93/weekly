import os
import datetime
import urllib.parse

def formatTime(timestamp):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

readmefile=open('README.md','w')
readmefile.write("# 潮流前端周刊\n")
recentfile=open('RECENT.md','w')

for root, dirs, filenames in os.walk('./md'):
  filenames.sort(reverse=True)

for index, name in enumerate(filenames):
    print(index)
    print(name)
    if name.endswith('.md'):
      filepath   = 'https://github.com/tw93/weekly/tree/main/md/' + urllib.parse.quote(name)
      modified = formatTime(os.path.getmtime('md/'+name))
      title = name.split('.md')[0]
      itemMd= '* [{}]({}) - {}\n'.format(title, filepath, modified)
      if index < 6
        recentfile.write(itemMd)
      readmefile.write(itemMd)

recentfile.close()
readmefile.close()

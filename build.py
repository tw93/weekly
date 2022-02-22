import os
import datetime
import urllib.parse

def formatGMTime(timestamp):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    dateStr = datetime.datetime.strptime(timestamp, GMT_FORMAT) + datetime.timedelta(hours=8)
    return dateStr.date()

readmefile=open('README.md','w')
readmefile.write("# 潮流前端周刊\n")
recentfile=open('RECENT.md','w')

for root, dirs, filenames in os.walk('./md'):
  filenames.sort(reverse=True)

for index, name in enumerate(filenames):
    print(index)
    print(name)
    if name.endswith('.md'):
      filepath   = 'https://github.com/tw93/weekly/tree/main/md' + urllib.parse.quote(name)
      modified = formatGMTime(os.path.getmtime(filepath))
      recentfile.write('* [{}]({}) - {}\n'.format(name, filepath, modified))
      readmefile.write('* [{}]({}/{})\n'.format(name,'md', urllib.parse.quote(name)))

readmefile.close()

import os
import urllib.parse

readmefile=open('README.md','w')
readmefile.write("# 潮流前端周刊\n")

for root, dirs, filenames in os.walk('./md'):
  filenames.sort(reverse=True)
  print(filenames)

for name in filenames:
    if name.endswith('.md'):
      readmefile.write('*  [{}]({}/{})\n'.format(name,'md', urllib.parse.quote(name)))

readmefile.close()

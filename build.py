import os
import urllib.parse

readmefile=open('README.md','w')
dir_ignore=['.git','.github']
readmefile.write("# 潮流前端周刊\n")
for root, dirs, filenames in os.walk('./md'):
  filenames.reverse()
  print(filenames)
# write relative link and names to readme.md
for name in filenames:
    if name.endswith('.md'):
      readmefile.write('*  [{}]({}/{})\n'.format(name,'md', urllib.parse.quote(name)))

readmefile.close()

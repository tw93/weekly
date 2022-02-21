import os
readmefile=open('README.md','w')
dir_ignore=['.git','.github']
readmefile.write("# 潮流前端周刊\n")
for filenames in os.walk('./md'):

print(filenames)
# write relative link and names to readme.md
for name in filenames:
    if name.endswith('.md'):
      readmefile.write('*  [{}]({}/{})\n'.format(name,'md',name))

readmefile.close()

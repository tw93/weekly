import os
readmefile=open('README.md','w')
dir_ignore=['.git','.github']
readmefile.write("# 潮流前端周刊\n")
for filenames in os.walk('./md'):
    #leaving the exceptional folders
    print(filenames);

print(filenames)
# write relative link and names to readme.md
for i in filenames:
    readmefile.write('*  [{}]({}/{})\n'.format(i,key,i))

readmefile.close()

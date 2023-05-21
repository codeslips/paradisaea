import json
import os
import random


def git_flow(m,path):
   if m == 'push':
      os.system(".\\utils\\git-push.bat " + '"'+path+'"')
      return True
   os.system(".\\utils\\git-commit.bat " + '"'+m+'"'+ " " + '"'+path+'"')
   return True

#git_flow('test py argument')




#m="'container frontend age function'"
def git_flow_backup(m):
    if m == 'push':
        os.system('git push')
        return True
    os.system('git add ../.')
    cm = 'git commit -m "%s"' % m
    os.system(cm)
#git_flow(m)
# automatically backup file

# KEYWORDS
# crontab
# cronjob
# shutil
# os
import os, shutil

path = '/Users/la/www/pythonAutoBackup' # use r for windows users ex. path = r'C:\directory' or path = 'C:\\directory'
dest = '/Users/la/www/pythonAutoBackup/backup' # use r for windows users ex. path = r'C:\directory' or path = 'C:\\directory'
# print(os.listdir(path))
allFiles = os.listdir(path)
# print(allFiles)

# AUTO COPY TO DESTINATION DIRECTORY
for a in allFiles:
    if a[-3:] != '.py' and a[0] != '.':
        try:
            source = os.path.join(path, a)
            destFiles = os.path.join(dest, a)
            # print(source)
            # print(a)
            shutil.copy2(source, destFiles)
        except:
            source = os.path.join(path, a)
            destFiles = os.path.join(dest, a)
            # print(source)
            # print(a)
            shutil.copytree(source, destFiles)

# print(os.listdir(dest))

# TASK SCHEDULE
'''
task schedule
create basic task
action
    new
        start program
        browse
        add arguments(optional):    "C:\DIRECTORY\autobackup.py"
        start in:   "C:\DIRECTORY\"
trigger
    daily
'''


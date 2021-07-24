# AUTO UPLOAD TO REMOTE SERVER DIRECTORY
import ftplib, os
server = 'uncle-test-server.com'
port = 2002
user = 'testuser@uncle-test-server.com'
password = "]6';bL;di"

ftp = ftplib.FTP()
ftp.connect(server, port)
ftp.login(user, password)

mypath = '/testcopyfile/pythonAutobackup'
enterpath = ftp.cwd(mypath)
# SINGLE FILE
'''
print('BEFORE', ftp.nlst())
filename = 'README.md'
fileupload = open(filename, 'rb')  # rb - read binary
result = ftp.storbinary('STOR '+ filename, fileupload)
print('RESULT', result)
print('AFTER', ftp.nlst())
ftp.quit()
'''
# LOOPING UPLOAD
allFiles = os.listdir(mypath)
for a in allFiles:
    if a[-3:] != '.py' and a[0] != '.':
        try:
            filename = os.path(mypath, a)
            fileupload = open(filename)
            result = ftp.storbinary('STOR '+ filename, fileupload)
        except:
            pass

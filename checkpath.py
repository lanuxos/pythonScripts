import os
imgfile = os.listdir('../asset/')
os.chdir('../asset/')
# mainpath = os.path.abspath(os.curdir) # get the current file location
mainpath = os.getcwd()  # get current working directory || current execute directory

pathlist = []

for img in imgfile:
    if img[-3:] == 'png' or img[-3:] == 'jpg':
        path = os.path.join(mainpath, img)
        print(path)
        pathlist.append(path)
import os


def scanfile(path):
    filelist = os.listdir(path)
    allfile = []
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            scanfile(filepath)
        print (filepath)


allfile = scanfile('\\\\192.168.18.163\\f$\\iso')
print(allfile)
##scanfile('\\\\192.168.18.163\\f$\iso')
#print(allfile)
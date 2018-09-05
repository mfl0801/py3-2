# -* coding:utf8 *-
import os,datetime
import sys
#filepath='\\\\192.168.18.163\\iso'
#filepath='\\\\192.168.18.100\\工具集'
filepath='\\\\192.168.18.163\\f$\iso'
tmppath='c:\\'
for i,o,p in os.walk(filepath):
    for name in p :
        if name.endswith(".iso") :
            print(os.path.join(i,name),os.path.getctime(filepath))
            #print(os.path.getctime(filepath))
print(os.listdir(filepath))


'''for i, o, p in os.walk(tmppath):
    for name in p:
        if name.endswith(".tmp"):
            print(os.path.join(i, name))'''




#    print("目录: %s" % i)
#    print("子目录: %s" % o)
 #   print("文件: %s" % p)
#size=os.path.(filepath)
#print(size)

#print("==========================")

#filelist=os.listdir(filepath)
#print(filelist)
'''filecopyname='cn_lync_2013_x86_x64_dvd_1145845.iso'
sourefilepath=filepath+'\\'+filecopyname
#print(sourefilepath)
desfilepath='d:\\test\\'
#os.popen(u"copy %s %s" % (sourefilepath,desfilepath ))
copycommand=os.popen("copy %s %s" % (sourefilepath,desfilepath ))
print(copycommand.read())
if copycommand == 0 :
    print("复制完成!")
desfilelist=os.listdir(desfilepath)
print(desfilelist)'''



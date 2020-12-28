import os
import re

path = '/Volumes/new/数据'

# 获取该目录下所有文件，存入列表中
f = os.listdir(path)

n = 0

print(len(f))
for i in range(len(f)):
    oldname = f[i]
    a = re.search("齿轮",oldname).span()
    b = re.search("-",oldname).span()
    c = re.search("-2020",oldname).span()
    num1 = int(f[i][a[1]:b[0]])
    num2 = int(f[i][b[1]:c[0]])
    newname = f[i][:a[1]] + "%03d" %num1  + "-" + "%03d"%num2 + ".txt"
    print(oldname)
    print(newname)

#
#     # #用os模块中的rename方法对文件改名
    os.rename(path +"/"+ oldname,path +"/"+ newname)
#     # print(oldname,'======>',newname)
#
#     n+=1

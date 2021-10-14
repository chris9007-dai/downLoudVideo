import re
import os

item = []   #存.ttml文件名
for files in os.listdir("./"): #读取当前文件夹.ttml文件名
    if os.path.splitext(files)[1] == '.ttml':
        item.append(files)
for files in os.listdir("./"): #读取当前文件夹.ttml文件名
    if os.path.splitext(files)[1] == '.mkv':
        item.append(files)

for index in range(len(item)):
    with open('/Users/mac/Desktop/downLoudCode/'+item[index],'r') as file:   #目标文件路径
        r=file.readlines()
    result=""
    for x in r:

        p1=re.findall(r">(.+?)</p>",x)   #正则，提取文本>,</p>之间的内容
        if(p1!=[]):
            res=p1[0]
            result+=res
    print(result)
    with open('/Users/mac/Desktop/newVideos/'+item[index].replace(".ttml",".txt"),'a+') as filewrite:   #存放地址
        filewrite.write(result)
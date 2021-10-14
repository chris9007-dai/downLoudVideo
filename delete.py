import os

filePath = []   #存.txt文件名
for files in os.listdir("./"): #读取当前文件夹.txt文件名
    if os.path.splitext(files)[1] == '.mp4':
        filePath.append(files)
    if os.path.splitext(files)[1] == '.ttml':
        filePath.append(files)
    if os.path.splitext(files)[1] == '.part':
        filePath.append(files)
    if os.path.splitext(files)[1] == '.mkv':
        filePath.append(files)
    if os.path.splitext(files)[1] == '.webm':
        filePath.append(files)
for file in filePath:#删除.txt文件
    if os.path.exists(file):
        os.remove(str(file))
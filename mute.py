from moviepy.editor import *

vfc = VideoFileClip
item = []   #存.mp4文件名
for files in os.listdir("./"): #读取当前文件夹.mp4文件名
    if os.path.splitext(files)[1] == '.mp4':
        item.append(files)
for files in os.listdir("./"): #读取当前文件夹.mp4文件名
    if os.path.splitext(files)[1] == '.webm':
        item.append(files)

for index in range(len(item)):  #视频批量消音
    old_video = "/Users/mac/Desktop/downLoudCode/"+ item[index]
    new_video = "/Users/mac/Desktop/newVideos/"+ item[index]
    video = VideoFileClip(old_video)
    video = video.without_audio()  # 删除声音，返回新的视频对象，原有对象不更改
    video.write_videofile(new_video)


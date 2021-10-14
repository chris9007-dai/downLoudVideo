#encoding=utf-8
import os
videolist = []
for line in open("./link.txt"):
    videolist.append(line)

for index in range(len(videolist)):
    os.system('youtube-dl --write-auto-sub --sub-lang zh-Hans --sub-format ttml '+ videolist[index])

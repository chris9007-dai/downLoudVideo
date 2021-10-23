<h1 align="center">执行文件说明<h1>
依赖包：moviepy ,youtube-dl

说明：在mac桌面新建downLoudCode，newVideos两个文件夹，downLoudCode用来存放git拉取的代码，newVideos用来存放执行后的视频，字幕。

​	windows则需要自行修改2.2，2.3中的代码地址

**1、将视频链接每行一个粘贴到link.txt中**

			例如： https://www.youtube.com/watch?v=sgtKab2ynrY
						https://www.youtube.com/watch?v=ROtvXKxFxhw

**2、脚本说明**

​		1、downloudviedeo.py			#该脚本读取link.txt中的链接并下载视频，字幕到当前文件夹

​		2、transitionTxt.py					#该脚本提取字幕中的文字 转存为txt文件

​		3、mute.py								#该脚本将视频消音

​															#上方2，3步骤执行后会生成新的文件，存在newVideo文件夹中，所以需要自己建个文件哦，可以在脚本中修改下方代码

```
with open('/Users/mac/Desktop/newVideos/'+item[index].replace(".ttml",".txt"),'a+') as filewrite:   #存放地址
```

​		4、delete.py								#删除当前文件夹的视频，字幕文件，你自己手动删也行，注意别错删脚本


from aip import AipSpeech
from videoLink import item


""" 你的 APPID AK SK """
APP_ID = '24765060'
API_KEY = 'wwZy2HtlteBxeWjlptEZzaX7'
SECRET_KEY = 'LPDdtlTq6DK7GVxuoixO4Hepq5KYNtvj'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
n=1

with open(r'/Users/mac/Desktop/6.txt','r') as file: #单个txt转mp3
    for line in file.readlines():
        print(line)

        result = client.synthesis(line, 'zh', 1, {'spd': 4.5, 'vol': 5, 'per': 5003})
        if not isinstance(result, dict):
            with open('/Users/mac/Desktop/1.mp3', 'ab+') as f:
                f.write(result)

""" for index in range(len(item)):
    with open('/Users/mac/Desktop/oldVideos/'+item[index].replace(".mp4",".zh-Hans.txt"),'r') as file:
    for line in file.readlines():
        print(line)

        result = client.synthesis(line, 'zh', 1, {'spd': 4.5, 'vol': 5, 'per': 5003})
        if not isinstance(result, dict):
            with open('/Users/mac/Desktop/newVideos/'+item[index]+".mp3", 'ab+') as f:
                f.write(result) """
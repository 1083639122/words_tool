import requests
import re
import os

with open('words1.txt','r')as f:
    words_list=f.read().split("\n")

print(words_list)

voice_list=[]
for i in words_list:
    try:
        res = requests.get('https://dict.eudic.net/dicts/en/'+i)
        slotList = re.findall(r'voice-js voice-button.*?/a',res.text)[1]
        if("amp;"in slotList):
            voice=re.findall(r'langid.*?"', slotList)[0].split('"')[0]
            voice_list.append('https://api.frdic.com/api/v2/speech/speakweb?'+re.sub("amp;","",voice))
        else:
            voice=re.findall(r'https:.*?.mp3', slotList)[0]
            voice_list.append(re.sub("amp;","",voice))
    except:
        voice_list.append("Can't find")


for i in voice_list:
    print(i)

print(len(words_list))
print(len(voice_list))
with open("voice.txt",'w')as f:
    for i in voice_list:
        f.writelines(i+'\n')

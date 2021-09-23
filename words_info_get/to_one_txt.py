with open('words1.txt','r')as f:
    words_list=f.read().split("\n")

with open('voice.txt','r')as f:
    voice_list=f.read().split("\n")

with open('meaning1.txt','r',encoding='utf8')as f:
    meaning_list=f.read().split("\n")

with open("words_info.txt",'w')as f:
    for i in range(0,len(words_list)):
        f.writelines(words_list[i]+'#'+voice_list[i]+'#'+meaning_list[i]+'#'+'\n')
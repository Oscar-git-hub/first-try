import requests
import re

url = 'https://www.cool18.com/bbs/index.php?app=forum&act=threadview&tid=14236299'

res = requests.get(url).text
p_info = 'src="(.*?)">.*?</center>'
info = re.findall(p_info, res, re.S)

for i in range(len(info)):
    if '.jpg' not in info[i]:
        info[i] = ''

while '' in info:
    info.remove('')

print(info)

for i in range(len(info)):
    p_pic = requests.get(info[i])
    file = open('图片' + str(i) + '.jpg', 'wb')
    file.write(p_pic.content)
    file.close()



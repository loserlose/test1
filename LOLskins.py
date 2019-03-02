import requests
import json
import re


start_url = "https://ossweb-img.qq.com/images/lol/web201310/skin/big"
url = "https://lol.qq.com/biz/hero/champion.js"
r = requests.get(url)
ret = r.text
#print(ret)
id_list = re.search('"keys":(.*),"data"',ret).group(1)
#print(id_list)
#print(type(id_list))
id_dict = json.loads(id_list)
#print(id_dict)
#print(type(id_dict))

val = input("是否确定下载(y/n):")

if val[-1] in ['y','Y'] :
    for i,j in id_dict.items():
        id=i
        name=j
        for k in range(4):
            result_url = start_url + id + '%03d' % k + '.jpg'
            print(result_url)

            if requests.get(result_url).status_code == 200:
                with open('img/%s%d.jpg' %(name,k),'wb') as f:
                    f.write(requests.get(result_url).content)
else:
    print("拜拜了您呐！！")
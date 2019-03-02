#最简单的爬虫结构
#利用网站抓包工具获取文件的url
#将文件爬取到对应的位置
import  requests

url = "https://m10.music.126.net/20190228210633/3cacecda77e3ad84146091b4a9b2ce0d/ymusic/15cf/1999/f76c/f7eb0f2df819a4493acd79095c6a647a.mp3"
with open('mp3/香水有毒.mp3','wb') as f:
    r = requests.get(url)
    f.write(r.content)
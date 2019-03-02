import requests
import re

#获取分类里面的小说
def get_novel_list():

    response = requests.get('http://www.quanshuwang.com/list/1_1.html')
    response.encoding = 'gbk'
    html = response.text
    #用正则表达式匹配每部小说的url
    reg = r'<a target="_blank" href="(.*?)" class="l mr10">'
    # print(re.findall(reg,html))
    return re.findall(reg,html)
#第二个函数  获取章节内容
def get_chapter_list(novel_url):

    response = requests.get('http://www.quanshuwang.com/book/170/170634')
    response.encoding = 'gbk'
    html = response.text
    reg = r'<a href="(.*?)" class="reader">'
    print(re.findall(reg,html))
    # return re.findall(reg, html)

for novel_url in get_novel_list():
    get_chapter_list(novel_url)
    break
    # print(novel_url)
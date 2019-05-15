import requests
import re
#模拟登陆
s = requests.Session()
#第一次请求 获取cookie
header={'Host': '10.28.102.51',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'}


r=s.get('http://10.28.102.51/student/logout.jsp',headers=header)

#print(r.headers['Set-Cookie'][0:-8])

#第二次请求 登陆
#构造data登录信息
while True:
    userName=input('账号:')
    passwd=input('密码:')
    if (userName[0] != 'Z') or (len(userName)!=9):
        print('输入不合法，重新输入\n')
    else:
        break
header2={'Host': '10.28.102.51',
'Connection': 'keep-alive',
'Content-Length': '85',
'Cache-Control': 'max-age=0',
'Origin': 'http://10.28.102.51',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Referer': 'http://10.28.102.51/student/logout.jsp',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cookie': r.headers['Set-Cookie'][0:-8]}

data1={'displayName':' ','displayPasswd':' ','submit':'%B5%C7++%C2%BC','userName':userName,'passwd':passwd}

q=s.post(url='http://10.28.102.51/student/checkUser.jsp',headers=header2,data=data1)

#print(q.text)
b=re.compile(r'登录成功',re.S)
if b.findall(q.text)[0]=='登录成功':
    print('登录成功\n')
else:
    exit()

    
#############输出登陆状态


##第三次请求 获取打卡信息

header3={'Host': '10.28.102.51',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Referer': 'http://10.28.102.51/student/checkUser.jsp',
'ccept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
'Cookie': r.headers['Set-Cookie'][0:-8],}

q1=s.get(url='http://10.28.102.51/student/queryExerInfo.jsp',headers=header3)



#######re
w=['','','','','','','','','','','','',]
k=['早操','体育俱乐部考勤','引体向上考勤','篮球比赛','田径','竞赛管理','考勤4','考勤5','增加次数','','','','',]
w[1]=re.compile(r'早操&nbsp;.*?&nbsp;([0-9]+?).*?次',re.S)
w[2]=re.compile(r'体育俱乐部考勤&nbsp;.*?&nbsp;([0-9]+?).*?次',re.S)
w[3]=re.compile(r'引体向上考勤&nbsp;.*?&nbsp;([0-9]+?).*?次',re.S)
w[4]=re.compile(r'篮球比赛&nbsp;.*?&nbsp;([0-9]+?).*?次',re.S)
w[5]=re.compile(r'田径&nbsp;.*?&nbsp;([0-9]+?).*?次',re.S)
w[6]=re.compile(r'竞赛管理&nbsp;.*?&nbsp;([0-9]+?).*?次',re.S)
w[7]=re.compile(r'考勤4&nbsp;.*?&nbsp;([0-9]+?).*?次',re.S)
w[8]=re.compile(r'考勤5&nbsp;.*?&nbsp;([0-9]+?).*?次',re.S)
w[9]=re.compile(r'增加次数&nbsp;.*?&nbsp;([0-9]+?).*?次',re.S)
xuehao=re.compile(r'学号:([A-Z][0-9]{8}.*?)',re.S)
xingmin=re.compile(r'姓名:(.*?)</b>',re.S)
print('学号',':',xuehao.findall(q1.text)[0],'\t','姓名:',xingmin.findall(q1.text)[0])

for i in range(9):
    w[i+1].findall(q1.text)
    print(k[i],':',w[i+1].findall(q1.text)[0])

input()




           



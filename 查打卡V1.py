import requests
import re
userName=''
passwd=''
while True:
    userName=input('学号:')
    passwd=input('密码:(直接回车为默认值)')
    if (len(userName)!=9):
        print('输入不合法，重新输入\n')
    else:
        break

if passwd.strip()=='':
	passwd=userName
#登录时需要POST的数据
post_data = {'displayName':' ', 
        'displayPasswd':' ', 
        'submit':'%B5%C7++%C2%BC', 
        'userName':userName,
        'passwd':passwd}

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}

#登录时表单提交到的地址（用开发者工具可以看到）
login_url = 'http://10.28.102.51/student/checkUser.jsp'

#构造Session
session = requests.Session()

#在session中发送登录请求，此后这个session里就存储了cookie
#可以用print(session.cookies.get_dict())查看
resp = session.post(login_url, post_data)

#登录后才能访问的网页
url = 'http://10.28.102.51/student/queryExerInfo.jsp'

#发送访问请求
resp = session.get(url)
resp_text=resp.text
#print(resp.text)

numbcarry=[0 for i in range(10)]
#早操 1
#print(resp_text)
"""个人信息获取截取"""
resp_text1=resp_text.split('早操')[0]
resp_text1=resp_text1.split('体锻信息查询')[2]

study_numb=re.search('学号:(.*?)&nbsp;',resp_text1)
study_numb=study_numb.group(1)
study_name=re.search('姓名:(.*?)</b>',resp_text1)
study_name=study_name.group(1)
#print(resp_text1)
#&nbsp;&nbsp;&nbsp;&nbsp;学号:056116101&nbsp;&nbsp;&nbsp;&nbsp;姓名:陈冬杰</b></td>
print('学号: '+study_numb+' 姓名: '+study_name)
"""打卡次数字符串截取"""
resp_text2=resp_text.split('早操')[1]
#print(resp_text2)
#体育俱乐部考勤 2
resp_text3=resp_text2.split('体育俱乐部考勤')[0]
#print(resp_text3)

num=re.search('(\d+)',resp_text3)
numbcarry[0]=int(num.group())
print('早操： '+str(numbcarry[0])+' 次')

resp_text2=resp_text2.split('体育俱乐部考勤')[1]

#引体向上考勤 3
resp_text3=resp_text2.split('引体向上考勤')[0]

num=re.search('(\d+)',resp_text3)
numbcarry[1]=int(num.group())
print('体育俱乐部考勤： '+str(numbcarry[1])+' 次')

resp_text2=resp_text2.split('引体向上考勤')[1]

#篮球比赛 4
resp_text3=resp_text2.split('篮球比赛')[0]

num=re.search('(\d+)',resp_text3)
numbcarry[2]=int(num.group())
print('引体向上考勤： '+str(numbcarry[2])+' 次')

resp_text2=resp_text2.split('篮球比赛')[1]

#田径 5
resp_text3=resp_text2.split('田径')[0]

num=re.search('(\d+)',resp_text3)
numbcarry[3]=int(num.group())
print('篮球比赛： '+str(numbcarry[3])+' 次')

resp_text2=resp_text2.split('田径')[1]
#运动会单项 6
resp_text3=resp_text2.split('运动会单项')[0]

num=re.search('(\d+)',resp_text3)
numbcarry[4]=int(num.group())
print('田径： '+str(numbcarry[4])+' 次')

resp_text2=resp_text2.split('运动会单项')[1]
#竞赛管理 7
resp_text3=resp_text2.split('竞赛管理')[0]

num=re.search('(\d+)',resp_text3)
numbcarry[5]=int(num.group())
print('运动会单项： '+str(numbcarry[5])+' 次')

resp_text2=resp_text2.split('竞赛管理')[1]
#考勤4 8
resp_text3=resp_text2.split('考勤4')[0]

num=re.search('(\d+)',resp_text3)
numbcarry[6]=int(num.group())
print('竞赛管理： '+str(numbcarry[6])+' 次')

resp_text2=resp_text2.split('考勤4')[1]
#考勤5 9
resp_text3=resp_text2.split('考勤5')[0]

num=re.search('(\d+)',resp_text3)
numbcarry[7]=int(num.group())
print('考勤4： '+str(numbcarry[7])+' 次')

resp_text2=resp_text2.split('考勤5')[1]
#增加次数 10
resp_text3=resp_text2.split('增加次数')[0]

num=re.search('(\d+)',resp_text3)
numbcarry[8]=int(num.group())
print('考勤5： '+str(numbcarry[8])+' 次')

resp_text2=resp_text2.split('增加次数')[1]
resp_text2=resp_text2.split('次')[0]
#print(resp_text2)
num=re.search('(\d+)',resp_text2)
numbcarry[8]=int(num.group())
print('增加次数： '+str(numbcarry[8])+' 次')
num_all=0
for i in range(10):
	num_all +=numbcarry[i]
print('总计： '+str(num_all)+' 次')
input()

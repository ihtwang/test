#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#发送邮箱
#sender = 'iht_wang@126.com'
sender = 'zhijunw@cn.ibm.com'
#接收邮箱
receiver = 'iht_wang@126.com'
#发送邮件主题
subject = 'Python email test'
#发送邮箱服务器
#smtpserver = 'smtp.126.com'
#smtpserver = 'pop.126.com'
smtpserver = r'C:\notes\data\mail1\zhijunw.nsf'
#发送邮箱用户/密码
#username = 'iht_wang@126.com'
#password = 'Wzj1234abcd20'

username = 'zhijunw@cn.ibm.com'
password = 'wzj1234abcd20'
#编写text 类型的邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()

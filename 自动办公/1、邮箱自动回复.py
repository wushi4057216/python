import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

host_server = 'smtp.sina.com'  #新浪邮箱smtp服务器
sender_sina = 'wushi123@sina.com'   #发件人邮箱
pwd = 'qwe123'   #邮箱密码

sender_sina_mail = 'wushi123@sina.com' #发件人邮箱
receiver = 'wushi456@sina.com'  #收件人邮箱

mail_title = 'Python办公自动化的邮件'  #邮件标题
mail_content = '你好，这是使用Python自动发送的邮件' #邮件的正文内容
mail_content1 = "你好，<p>这是使用Python自动发送的邮件</p><p><a href='http://python.cn'> python</p> " #邮件的正文内容


#构造邮件主题
msg = MIMEMultipart()
msg['Subject'] = Header(mail_title, 'utf-8')
msg['From'] = sender_sina_mail
msg['To'] = Header('测试邮箱', 'utf-8')
msg.attach(MIMEText(mail_content, 'plain', 'utf-8')) #plain是无格式发送，html是网页格式发送内容

msg.attach(MIMEText(mail_content, 'html', 'utf-8'))   #发送带格式的网页
att = MIMEApplication(open('D:/123.doc', 'rb').read()) #添加附件
att.add_header('Content-Disposition', 'attachment', filename='test.doc') #附件重命名
msg.attach(att)  #给邮件添加附件

#登录邮箱发送
try:
    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_sina, pwd)
    smtp.sendmail(sender_sina_mail, receiver, msg.as_string())
    smtp.quit()
    print('邮件发送成功')
except smtplib.SMTPException:
    print('邮件发送失败')


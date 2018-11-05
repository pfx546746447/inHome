# _*_ coding: utf-8 _*_

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "18045386228@163.com"  # 用户名
mail_pass = "Aa123456"  # 口令

sender = '天翼空间每日apk检查'
receivers = '546746447@qq.com,447038337@qq.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱



class SendMail(object):

    def __init__(self, header, mail_host, mail_user, mail_pass, sender, receivers):
        '''
        :param header: mail title
        :param mail_host: 邮箱smtp的域名
        :param mail_user: 邮箱smtp帐号
        :param mail_pass: 邮箱smpt帐号密码
        :param sender: 邮箱发送者
        :param receivers: 邮箱接收者，多人就排版成用逗号分割开的字符串
        '''
        self.header = header
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.sender = sender
        self.receivers = receivers

    def send_mail(self, type='html', content=''):
        '''
        :param type:
        :param content:
        :return:
        '''
        msg = ''
        if type == 'html':
            msg = MIMEText(content, 'html', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
        elif type == 'txt':
            msg = MIMEText(content, 'txt', 'utf-8')
        msg['Subject'] = Header(self.header, 'utf-8')
        msg['From'] = self.mail_user
        msg['To'] = self.receivers

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers.split(','), msg.as_string())
            print "邮件发送成功"
        except smtplib.SMTPException as e:
            print e
            print "Error: 发送邮件失败"
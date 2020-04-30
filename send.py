#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import random


sender=['fangyuchu@mail.bugless.club','fang@mail.bugless.club','victorfang@mail.bugless.club','fyc@mail.bugless.club','csnetwork@mail.bugless.club']

def send_email(receiver,text,From,To,subject):
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header(From, 'utf-8')
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    random.shuffle(sender)
    # print(sender[0])

    try:
        smtpObj = smtplib.SMTP('localhost')
        # smtpObj.set_debuglevel(True)
        smtpObj.sendmail(sender[0], receiver, message.as_string())
        smtpObj.close()
        print("给"+To+"的邮件发送成功")
    except smtplib.SMTPException:
        print("Error:" "无法给"+To+"发送邮件")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from HtmlTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib, getpass, time, os, unittest

def send_mail(file_new):
    smtpserver = input('Enter your smtp server:')
    user_account = input("Enter your user account:")
    pw = getpass.getpass("Enter your password:")
    sender = user_account
    receiver = input("Enter your receiver:")

    # https://docs.python.org/3/library/time.html#time.strftime
    # time.strftime(format[, t])
    # If t is not provided, the current time as returned by localtime() is used.
    subject ='自動化測試報告' + time.strftime(" %Y-%m-%d %H:%M:%S")
    with open(file_new, 'rb') as fp:
        content = fp.read()

    # msg = MIMEText(content, 'html', 'utf-8')
    msg = MIMEMultipart('mixed')
    html_attach = MIMEText(content, 'html', 'utf-8')
    html_attach["Content-Disposition"] = 'attachment; filename="attach.html"'
    msg.attach(html_attach)

    text = 'Hi你好,\n\t請見測試附檔'
    text_plain = MIMEText(text, 'plain', 'utf-8') 
    msg.attach(text_plain)
    
    msg['Subject'] = Header(subject, 'utf-8')
    # msg['From'] = sender
    msg['From'] = Header("{0}".format("測試者"), 'utf-8') # sender's name
    print(msg['From'])
    msg['To'] = receiver
    # msg['To'] = Header("{0} <{1}>".format("我是誰", receiver), 'utf-8') # not working
    # msg['To'] = Header("{0}".format("我是誰"), 'utf-8') # only "我是誰"
    print(msg['To'])
    print(msg)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 587) # 傳輸層安全性 (TLS)/STARTTLS 通訊埠：587
    
    # Perform the login step after you've started TLS.
    smtp.ehlo()
    smtp.starttls()
    try:
        smtp.login(user_account, pw)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except:
        raise
    else:
        print('email has send out')

def new_report(folder):
    lists = os.listdir(folder)
    #重新按時間對目錄下的檔進行排列
    lists.sort(key=lambda fn: os.path.getmtime(folder+"\\"+fn))
    print('最新的文件為： ' + lists[-1])
    file_latest = os.path.join(folder, lists[-1])
    print('最新的文件為： ' + file_latest)
    return file_latest

def run_test():
    # test_dir = './test_project/test_case'
    test_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_sta.py')
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(output='example_suite') # https://github.com/oldani/HtmlTestRunner
    # Just import HtmlTestRunner from package, then pass it to unittest.main with the testRunner keyword. 
    # This class have only one required parameter, with is output this is use to place the report of the TestCase, 
    # this is saved under a reports directory.
    runner.run(discover)

if __name__ == '__main__':
    run_test()
    # result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir, "reports", "example_suite")
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports", "example_suite")
    file_new = new_report(result_dir)
    send_mail(file_new)

    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>python ch09\run_selenium-server.py
    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch11>python runtest.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from HtmlTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib, getpass, time, os, unittest

def attach_files(msg, file_new):
    for i, v in enumerate(file_new):
        with open(v, 'rb') as fp:
            content = fp.read()
        html_attach = MIMEText(content, 'html', 'utf-8')
        # html_attach["Content-Disposition"] = 'attachment; filename="attach' + str(i + 1) + '.html"'
        name = v.split('/')[-1]
        html_attach["Content-Disposition"] = 'attachment; filename="' + name + '"'
        msg.attach(html_attach)
    return msg

def send_mail(file_new):
    smtpserver = input('Enter your smtp server:')
    user_account = input("Enter your user account:")
    pw = getpass.getpass("Enter your password:")
    sender = user_account
    receiver = input("Enter your receiver:")

    # msg = MIMEText(content, 'html', 'utf-8')
    msg = MIMEMultipart('mixed')
    
    # with open(file_new, 'rb') as fp:
        # content = fp.read()
    # html_attach = MIMEText(content, 'html', 'utf-8')
    # html_attach["Content-Disposition"] = 'attachment; filename="attach.html"'
    # msg.attach(html_attach)   
    msg = attach_files(msg, file_new)

    # https://docs.python.org/3/library/time.html#time.strftime
    # time.strftime(format[, t])
    # If t is not provided, the current time as returned by localtime() is used.    
    subject ='自動化測試報告' + time.strftime(" %Y-%m-%d %H:%M:%S")

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
    # print(msg)

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
    lists.sort(key=lambda fn: os.path.getmtime(folder+"/"+fn))
    print('最新的文件為： ' + lists[-1])
    file_latest = os.path.join(folder, lists[-1])
    print('最新的文件為： ' + file_latest)
    return file_latest

# def files_in_a_period_of_time(folder, lists, seconds):
def files_in_a_period_of_time(folder, seconds):
    lists = os.listdir(folder)
    ret = []
    print('folder', folder)
    print()
    print('lists', lists)
    print()
    for f in lists:
        st = os.stat(folder + "/" + f)
        # st = os.stat(os.path.join(folder, f))
        mtime = st.st_mtime
        if time.time() - mtime < seconds:
            f = folder + "/" + f
            # f = os.path.join(folder, f)
            ret.append(f)
    return ret

def run_test():
    test_dir = './test_project/test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(output='example_suite') # https://github.com/oldani/HtmlTestRunner
    # Just import HtmlTestRunner from package, then pass it to unittest.main with the testRunner keyword. 
    # This class have only one required parameter, with is output this is use to place the report of the TestCase, 
    # this is saved under a reports directory.

    runner.run(discover)

if __name__ == '__main__':
    run_test()
    result_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir, "reports", "example_suite")
    print(result_dir)
    result_dir = result_dir.replace('\\', '/')
    print(result_dir)
    # file_new = new_report(result_dir)
    file_new = files_in_a_period_of_time(result_dir, 60)
    print()
    print('file_new', file_new)
    send_mail(file_new)

    # test_dir = './test_project/test_case'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    # runner = HTMLTestRunner(output='example_suite') # https://github.com/oldani/HtmlTestRunner
    # runner.run(discover)

    # (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch08>python test_project\runtest_send_mail_multi-attachment.py
    
    # Running tests...
    # ----------------------------------------------------------------------
    # test_baidu (test_baidu.MyTest) ... OK (10.244832)s
    # test_youdao (test_youdao.MyTest) ... OK (11.589231)s
    
    # ----------------------------------------------------------------------
    # Ran 2 tests in 0:00:21
    
    # OK
    
    
    
    # Generating HTML reports...
    # C:\Users\Han\selenium_test\ch08\test_project\..\reports\example_suite
    # C:/Users/Han/selenium_test/ch08/test_project/../reports/example_suite
    # folder C:/Users/Han/selenium_test/ch08/test_project/../reports/example_suite
    
    # lists ['Test_test_baidu.MyTest_2018-04-05_02-56-45.html', 'Test_test_baidu.MyTest_2018-04-05_02-58-59.html', 'Test_test_youdao.MyTest_2018-04-05_02-56-45.html', 'Test_test_youdao.MyTest_2018-04-05_02-58-59.html']
    
    
    # file_new ['C:/Users/Han/selenium_test/ch08/test_project/../reports/example_suite/Test_test_baidu.MyTest_2018-04-05_02-58-59.html', 'C:/Users/Han/selenium_test/ch08/test_project/../reports/example_suite/Test_test_youdao.MyTest_2018-04-05_02-58-59.html']
    # Enter your smtp server:
    # Enter your user account:
    # Enter your password:
    # Enter your receiver:
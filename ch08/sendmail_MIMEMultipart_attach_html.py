#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
import getpass

def to_addr(addr, str, target):
    while True:
        mail = input("Enter your " + target + " (type quit to exit):")
        if mail == 'quit':
            if str != 'Bcc': # The headers in the email body will include only the TO: and CC
                msg[str] = ','.join(addr) # assign to header after typing 'quit'
            break
        addr.append(mail)

smtpserver = input('Enter your smtp server:')
user_account = input("Enter your user account:")
pw = getpass.getpass("Enter your password:")
sender = user_account

# class email.mime.multipart.MIMEMultipart(_subtype='mixed', boundary=None, _subparts=None, *, policy=compat32, **_params)
msg = MIMEMultipart('mixed')
subject ='Python email attach html test read 14'
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender


mail_to = []
to_addr(mail_to, 'To', 'recipient')
mail_cc = []
to_addr(mail_cc, 'Cc', 'cc')
mail_bcc = []
to_addr(mail_bcc, 'Bcc', 'bcc')
# msg['To'] = mail_to
# msg['Cc'] = mail_cc
# msg['Bcc'] = mail_bcc # The headers in the email body will include only the TO: and CC
print(msg)

recipient = []
# recipient.append(mail_to)
# recipient.append(mail_cc)
# recipient.append(mail_bcc)
recipient = mail_to + mail_cc + mail_bcc # do not use s.append(x), use "+" into one list
print(recipient)


# attach html
html_msg = """
<p>Real</p>
<p><a href="http://blog.real-yj.com/">Real</a></p>
<p>Real 14：</p>
<p><img src="real-14.jpg"></p>
"""

html_attach = MIMEText(html_msg, 'html', 'utf-8')
html_attach["Content-Disposition"] = 'attachment; filename="attach.html"'
msg.attach(html_attach)

# attach html jpg file for <img src="real-14.jpg">
# att2 = MIMEImage(open('real-14.jpg','rb').read())
with open('real-14.jpg', 'rb') as fp:
    img_data = fp.read()
att2 = MIMEImage(img_data)

# att2.add_header('Content-ID', '<image1>')
att2.add_header('Content-Disposition', 'attachment; filename="real-14.jpg"')
msg.attach(att2)


smtp = smtplib.SMTP()
smtp.connect(smtpserver, 587) # 傳輸層安全性 (TLS)/STARTTLS 通訊埠：587

# Perform the login step after you've started TLS.
smtp.ehlo()
smtp.starttls()

smtp.login(user_account, pw)
smtp.sendmail(sender, recipient, msg.as_string())
smtp.quit()


# >>> from email.mime.text import MIMEText
# >>> msg = MIMEText('<html><h1>你好</h1></html>', 'html', 'utf-8')
# >>> type(msg)
# <class 'email.mime.text.MIMEText'>
# >>> print(msg)
# Content-Type: text/html; charset="utf-8"
# MIME-Version: 1.0
# Content-Transfer-Encoding: base64

# PGh0bWw+PGgxPuS9oOWlvTwvaDE+PC9odG1sPg==

# >>> msg.as_string()
# 'Content-Type: text/html; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\n\nPGh0bWw+PGgxPuS9oOWlvTwvaDE+PC9odG1sPg==\n'
# >>> print(msg)
# Content-Type: text/html; charset="utf-8"
# MIME-Version: 1.0
# Content-Transfer-Encoding: base64

# PGh0bWw+PGgxPuS9oOWlvTwvaDE+PC9odG1sPg==

# >>> subject ='Python email test'
# >>> from email.header import Header
# >>> msg['Subject'] = Header(subject, 'utf-8')
# >>> print(msg)
# Content-Type: text/html; charset="utf-8"
# MIME-Version: 1.0
# Content-Transfer-Encoding: base64
# Subject: =?utf-8?q?Python_email_test?=

# PGh0bWw+PGgxPuS9oOWlvTwvaDE+PC9odG1sPg==

# >>> msg.as_string()
# 'Content-Type: text/html; charset="utf-8"\nMIME-Version: 1.0\nContent-Transfer-Encoding: base64\nSubject: =?utf-8?q?Python_email_test?=\n\nPGh0bWw+PGgxPuS9oOWlvTwvaDE+PC9odG1sPg==\n'
# >>>






# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch08>python sendmail.py
# Enter your smtp server:smtp.gmail.com
# Enter your user account:xxx@gmail.com
# Enter your password:
# Enter your receiver:xxxxx@gmail.com
# Traceback (most recent call last):
  # File "sendmail.py", line 19, in <module>
    # smtp.login(user_account, pw)
  # File "C:\Users\Han\Anaconda3\lib\smtplib.py", line 697, in login
    # "SMTP AUTH extension not supported by server.")
# smtplib.SMTPNotSupportedError: SMTP AUTH extension not supported by server.


# SMTP AUTH extension not supported by server.

# https://stackoverflow.com/questions/39686141/smtp-auth-extension-not-supported-by-server-in-python
# http://zhjwpku.com/2017/02/14/smtp-auth-extension-not-supported-by-server.html

# solution: use smtp.ehlo() and smtp.starttls()




# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test\ch08>python sendmail.py
# Enter your smtp server:smtp.gmail.com
# Enter your user account:xxx@gmail.com
# Enter your password:
# Enter your receiver:xxxxx@gmail.com
# Traceback (most recent call last):
  # File "sendmail.py", line 24, in <module>
    # smtp.login(user_account, pw)
  # File "C:\Users\Han\Anaconda3\lib\smtplib.py", line 730, in login
    # raise last_exception
  # File "C:\Users\Han\Anaconda3\lib\smtplib.py", line 721, in login
    # initial_response_ok=initial_response_ok)
  # File "C:\Users\Han\Anaconda3\lib\smtplib.py", line 642, in auth
    # raise SMTPAuthenticationError(code, resp)
# smtplib.SMTPAuthenticationError: 


# gmail

# 查看遭拒的登入嘗試 
        
# 您好：
# Google 剛剛已禁止某人透過可能會危害你帳戶的應用程式登入你的 Google 帳戶 

# 嘗試登入者是您本人嗎？
# 您所使用的應用程式有已知的安全性問題或版本過舊，因此 Google 將繼續禁止該應用程式登入帳戶。如要繼續使用這個應用程式，您可以啟用低安全性應用程式的存取權限，但這樣會導致帳戶安全性降低。

# solution: 啟用允許安全性較低的應用程式

# 低安全性應用程式

# 由於部分應用程式和裝置採用安全性較低的登入技術，您的帳戶會因此出現安全漏洞。建議您取消這些應用程式的存取權限；如果您瞭解有風險，但還是要使用這些應用程式，則可以開放存取權限。 瞭解詳情

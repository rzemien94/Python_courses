import smtplib

mailFrom = 'Your automation system'
mailTo = ['rzmientest@op.pl']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello

This mail confirms that processing has finished without problems,

Have a nice day!'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)

user = input('login to mail:')
password = input('password to mail:')

try:
    server = smtplib.SMTP_SSL('smtp.poczta.onet.pl', 465)
    print('connected')
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')
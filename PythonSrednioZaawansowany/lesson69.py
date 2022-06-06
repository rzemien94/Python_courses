import smtplib
import functools

def send_email(mail_to,mail_from,mail_subject,mail_body):
    message = '''From: {}
    Subject: {}
    
    {}
    '''.format(mail_from, mail_subject, mail_body)

    user = input('login to mail:')
    password = input('password to mail:')

    try:
        server = smtplib.SMTP_SSL('smtp.poczta.onet.pl', 465)
        print('connected')
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mail_to, message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending email',e)
        return False

mail_from = 'Your automation system'
mail_to = ['rzmientest@op.pl']
mail_subject = 'Processing finished successfully'
mail_body = '''Hello

This mail confirms that processing has finished without problems,

Have a nice day! Partial'''

send_email_onet = functools.partial(send_email, mail_to,mail_subject='execution alert')

send_email_onet(mail_from=mail_from,mail_body=mail_body)
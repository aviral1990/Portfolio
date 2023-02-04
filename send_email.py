import smtplib,ssl

host="smtp.gmail.com"
port = 465


username="aviral18@gmail.com"
password="nmopuluqxihzibza"

context=ssl.create_default_context()
receiver="macto.cognatus.90@gmail.com"             #
message="""\
Subject: Hola
I Love You
:*
"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)

import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "daithileonard@gmail.com"
password = "ecwvfmndasfhrsmh"

receiver = "daithileonard@gmail.com"
context = ssl.create_default_context()
message = """\
Subject: Portfolio business request
Hi
This is the email message
thanks
David
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
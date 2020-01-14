# Sending email with attachment

attachment = 'FILE_PATH'

file = open(latest_file, "rb")
part = MIMEApplication(file.read(), Name=basename(attachment))
file.close()

part['Content-Disposition'] = 'attachment; filename="%s"' % basename(latest_file)

msg = MIMEMultipart()
part1 = MIMEText("Email message text goes here", 'plain')

from_email = 'from-email@host.com'
msg['Subject'] = 'Email Subject'
msg.attach(part1)

to_emails = ['recipient1@host.com', 'recipient2@host.com', 'recipient3@host.com']
msg['From'] = from_email
msg['To'] = ", ".join(to_emails)

msg.attach(part)

smtp = smtplib.SMTP()
smtp.connect('SMTP_SERVER', SMTP_PORT
smtp.login('SMTP_USER', 'SMTP_PASSWORD')
smtp.sendmail(from_email, to_emails, msg.as_string())
smtp.close()

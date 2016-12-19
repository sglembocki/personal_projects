#Script to open Excel file, refresh it, and automatically send email with attachment(s)
import win32com.client
import shutil
import time

#Set file path
SourcePathName = '' #Update path here
FileName = 'file.xlsx' #Update file name here

#Open Excel
Application = win32com.client.Dispatch("Excel.Application")
Application.Visible = True #Show Excel. While this is not required, it can help with debugging

#Open and refresh Excel file
Workbook = Application.Workbooks.open(SourcePathName + '/' + FileName) #Open the Workbook
Workbook.RefreshAll() #Refesh all
time.sleep(10) #Pause
Workbook.Save() #Saves the workbook
time.sleep(5) #Pause

#Closes Excel
Application.Quit()

#Send email (all steps below)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Set email variables
me = ''
you = ['', '']

msg = MIMEMultipart('alternate')
msg['Subject'] = ""
msg['From'] = me
msg['To'] = ''
msg['Cc'] = ''

#Html format
html = """\
	<html>
		<head></head>
		<body>
			<p>
				Insert email text here
			</p>
		</body>
	</html>
"""

#Message rendered as html
part1 = MIMEText(html, 'html')

#Excel file attachment
part3 = MIMEBase('application', "octet-stream")
part3.set_payload(open("", "rb").read())
encoders.encode_base64(part3)
part3.add_header('Content-Disposition', 'attachment; filename = "file.xlsx"')

#Message attachments
msg.attach(part1)
msg.attach(part3)

#Connect to SMTP server
s = smtplib.SMTP()
s.connect('', '') #Email server, port
s.ehlo()
s.starttls()
s.login('', '') #Embed credentials here. Username, password

#Send email and close
s.set_debuglevel(1)
s.sendmail(me, ['', ''], msg.as_string()) #From, to, and message
s.quit() #Close connection, end of script
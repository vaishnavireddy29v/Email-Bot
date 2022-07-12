import smtplib
import speech_recognition as sr
import pyttsx3
import imaplib
import http.client
import email.parser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
listener = sr.Recognizer()
engine = pyttsx3.init()
def talk(text):
 engine.say(text)
 engine.runAndWait()
def get_info():
 try:
 with sr.Microphone() as source:
 print("listening.....")
 voice = listener.listen(source)
 info= listener.recognize_google(voice)
 print(info)
 return info.lower()
 except:
 pass
talk("hello how can I help you?")
help = get_info()
if "inbox" in help:
 host = 'imap.gmail.com'
 username = 'saverirangavajula@gmail.com'
 password = '*********'
 talk("this is your inbox")
10 | P a g e
 def get_inbox():
 mail = imaplib.IMAP4_SSL(host)
 mail.login(username, password)
 mail.select("inbox")
 _, search_data = mail.search(None, 'UNSEEN')
 my_message = []
 for num in search_data[0].split():
 email_data = {}
 _, data = mail.fetch(num, '(RFC822)')
 # print(data[0])
 _, b = data[0]
 email_message = email.message_from_bytes(b)
 for header in ['subject', 'to', 'from', 'date']:
 print("{}: {}".format(header, email_message[header]))
 email_data[header] = email_message[header]
 for part in email_message.walk():
 if part.get_content_type() == "text/plain":
 body = part.get_payload(decode=True)
 email_data['body'] = body.decode()
 elif part.get_content_type() == "text/html":
 html_body = part.get_payload(decode=True)
 email_data['html_body'] = html_body.decode()
 my_message.append(email_data)
 return my_message
 if __name__ == "__main__":
 my_inbox = get_inbox()
 print(my_inbox)
def send_email(receiver,subject,message):
 server = smtplib.SMTP('smtp.gmail.com',587)
 server.starttls()
 server.login('saverirangavajula@gmail.com','********')
 email=EmailMessage()
 email['From']='saverirangavajula@gmail.com'
 email['To'] = receiver
 email['Subject']= subject
 email.set_content(message)
 yesorno = get_info()
 if yesorno=="no":
 server.send_message(email)
11 | P a g e
 talk("email sent successfully")
 else:
 talk("what file")
 n = get_info()
 filename = file_list[n]
 with open(filename,"rb") as f:
 file_data = f.read()
 
email.add_attachment(file_data,maintype="application",subtype="npg",filena
me=filename)
 server.send_message(email)
 talk('attachment sent')
email_list = {
 'black': 'i.navakanth@gmail.com',
 'pink': 'vaishnavireddy1280@gmail.com',
 "red":'shylaranitekmal@gmail.com'
}
file_list = {
 'sample 1' : "photo.png",
 'sample 2' : "output2.xml",
 'sample 3': "output3.doc"
}
if "send" in help:
 def get_email_info():
 talk('to whom you want to send email')
 name = get_info()
 receiver = email_list[name]
 print(receiver)
 talk('what is the subject')
 subject = get_info()
 talk('tell me the text')
 message = get_info()
 talk("do you want to attach files")
 send_email(receiv0e0.r,subject,message)
 get_email_info()

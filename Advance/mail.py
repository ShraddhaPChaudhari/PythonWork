#sending mail through python
import smtplib
server=smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.ehlo()
server.login("shraddhachaudhari810@gmail.com","password")
msg="hello"
server.sendmail("shraddhachaudhari810@gmail.com","shraddhachaudhari810@gmail.com",msg)
print("sent sucessfully")

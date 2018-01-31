# Sending email

import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("jayantkendole.jk@gmail.com", "ForPython1")
 
msg = "Hi"
server.sendmail("jayantkendole.jk@gmail.com", "jayant.17ec@cmr.edu.in", msg)
server.quit()

import smtplib as sm,ssl

context = ssl.create_default_context() 
with sm.SMTP("smtp.gmail.com", 587) as smtpClient:
    # smtpClient.ehlo()
    smtpClient.starttls(context=context)
    smtpClient.login('vikaskumar637884@gmail.com', 'Vikas@#$kumarisgreat')
    subject = 'Only for testing'
    body = 'I love python'
    message = "subject:{}\n{}".format(subject, body)
    receivers = ['vikas.271573@gmail.com',
           'vikas1618072@gmail.com']
    smtpClient.sendmail('vikaskumar637884@gmail.com', receivers, message)
    print("Your mail successfully send")
    smtpClient.quit() 
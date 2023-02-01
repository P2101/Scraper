import smtplib

def send_mail(message, name):
    # WE START THE SERVICE
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("abc@gmail.com", "fsdfdsfdsxdfxk") # Password MUST be App Pasword (ENCODED)
    Message = (f"Apartement --> {name} \n\n {message}") # Message WE WANT TO SEND
    server.sendmail("abc@gmail.com", "dfc@gmail.com", Message) # FROM WHOM TO WHOM AND THE MESSAGE
    print("Mail has been sent!")
    server.quit() # FINALLY WE CLOSE THE SERVER

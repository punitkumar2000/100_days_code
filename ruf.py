# # import smtplib
# # import ssl
# # from email.message import EmailMessage

# # # Define email sender and receiver
# # email_sender = 'punit.kumar@knowlarity.com'
# # email_password = 'Punit@9599'
# # email_receiver = 'akshay.jain@knowlarity.com'

# # # Set the subject and body of the email
# # subject = 'Check out my new video!'
# # body = """
# # I've just published a new video on YouTube: https://youtu.be/2cZzP9DLlkg
# # """

# # em = EmailMessage()
# # em['From'] = email_sender
# # em['To'] = email_receiver
# # em['Subject'] = subject
# # em.set_content(body)

# # # Add SSL (layer of security)
# # context = ssl.create_default_context()

# # # Log in and send the email
# # with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
# #     smtp.login(email_sender, email_password)
# #     smtp.sendmail(email_sender, email_receiver, em.as_string())



# # pip install validate-email-address
# # pip install py3dns
# # from validate_email_address import validate_email
# # isvalid=validate_email('punit.kumar@knowlarity.com')
# # print(isvalid, "1")
# # from validate_email_address import validate_email
# # isExists = validate_email('punit.kumar@knowlarity.com', verify=True)
# # print(isExists, "2")

# # pip install validate_email

# # from validate_email import validate_email
# # is_valid = validate_email('punitmann9599@gmail.com',verify=True)
# # print(bool(is_valid))

# # import dnspython
# # from validate_email_address import validate_email
# # isExists = validate_email('punitmann9599@gmail.com', verify=True)
# # print(isExists)



# # from datetime import datetime
# # from verify_email import verify_email
# # from verify_email import *
# # import multiprocessing


# # emails = ["punitmann9599@gmail.com"]  # add emails
# # b = datetime.now()


# # def validate(email):
# #     a = datetime.now()
# #     value = verify_email(email)
# #     delta = datetime.now() - a
# #     print(value, email, (delta.microseconds + delta.microseconds/1E6))


# # pool = multiprocessing.Pool()
# # result = pool.map(validate, emails)
# # delta = datetime.now() - b
# # print(delta.total_seconds())


# # import requests

# # email_address = "punitoiohoghma2@knowlarity.com"
# # response = requests.get(
# #     "https://isitarealemail.com/api/email/validate",
# #     params = {'email': email_address})

# # status = response.json()['status']
# # print(status)
# # if status == "valid":
# #   print("email is valid")
# # elif status == "invalid":
# #   print("email is invalid")
# # else:
# #   print("email was unknown")

# import requests

# # email_address = "punitoiohoghma2@knowlarity.com"
# # response = requests.get(
# #     "https://isitarealemail.com/api/email/validate",
# #     params = {'email': email_address})

# # status = response.json()['status']
# # if status == "valid":
# #   print("email is valid")
# # elif status == "invalid":
# #   print("email is invalid")
# # else:
# #   print("email was unknown")

# # from verify_email import verify_email
# # print(verify_email('punitmann9599@gmail.com'))

# email_sender = 'punit.kumar@knowlarity.com'
# email_password = 'Punit@mann'
# email_receiver = "punit.kumar@knowlarity.com"

# # Set the subject and body of the email
# subject = "Agent Account has been Created for user {username}"
# body = """
# The Agent Account has been Successfully created.
# Email ID - {email}
# Password - {password}
# Click this link to login : https://speechanalytics.knowlarity.ai/index.html
# """

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# # Add SSL (Secure Sockets Layer)
# context = ssl.create_default_context()

# # Log in and send the email
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())

import dns
from email_validator import validate_email, EmailNotValidError, caching_resolver

email = "punitmann9599@gmail.com"
is_new_account = True # False for login pages
resolver = caching_resolver(timeout=10)

try:
  # Check that the email address is valid.
    while True:
        validation = validate_email(email, dns_resolver=resolver)

        # Take the normalized form of the email address
        # for all logic beyond this point (especially
        # before going to a database query where equality
        # may not take into account Unicode normalization).  
        email = validation.email
except EmailNotValidError as e:
  # Email is not valid.
  # The exception message is human-readable.
  print(str(e))

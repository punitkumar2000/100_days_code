import smtplib

email = "checkcheckpython@gmail.com"
password = "Check@9599"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password = password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg="Subject:Hello\n\n This is the body of the email."
    )
connection.quit()
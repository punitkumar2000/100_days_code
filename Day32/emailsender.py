import smtplib

email = "punit.kumar@knowlarity.com"
password = "Punit@mann"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password = password)
    connection.sendmail(
        from_addr=email,
        to_addrs="punit.kumar@knowlarity.com",
        msg="Subject:Hello\n\n This is the body of the email."
    )
connection.quit()
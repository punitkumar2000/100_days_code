from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "punitmann9599@gmail.com"
PASSWORD = ""

today = datetime.now()
month = today.month
day = today.day
today_tuple = (today.month, today.day)

data = pandas.read_csv("Day32/AutomatedBirthdayWisher/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"Day32/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com", ) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addrs=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday \n\n {contents}"
        )
        
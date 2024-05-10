import datetime as dt
import random
import pandas
import smtplib

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("./birthdays.csv")

birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    random_letter = random.randint(1, 3)
    letter_path = f"letter_templates/letter_{random_letter}.txt"

    with open(letter_path, "r") as file:
        letter_content = file.read()

    person_data = (birthdays_dict[today])
    person_name = person_data['name']

    letter_content = letter_content.replace('[NAME]', person_name)

    my_email = "myemail@gmail.com"
    password = "**********"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="test@gmail.com",
                            msg=f"Subject:Happy Birthday!\n\n{letter_content}")







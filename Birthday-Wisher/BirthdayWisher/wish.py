import random
from datetime import datetime
import smtplib
import pandas

MY_EMAIL = "zubairansariinfo941@gmail.com"
password = "eyfs cdvw kurd lwsk"


today = datetime.now()
today_touple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]):data_row for index, data_row in data.iterrows()}
if today_touple in birthday_dict:
    person = birthday_dict[today_touple]
    filePath = f"D:/50-days/Birthday-Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filePath) as file:
        content = file.read()
        content = content.replace("[NAME]", person["name"])
        print(content)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:Happy Birthday\n\n {content}")
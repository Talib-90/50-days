import smtplib
import datetime as dt
import random

MY_EMAIL = "zubairansariinfo941@gmail.com"
password = "eyfs cdvw kurd lwsk"

now = dt.datetime.now()
weekDay = now.weekday()
print(weekDay)
if weekDay == 1:
    with open("quotes.txt") as dataFile:
        allQuotes = dataFile.readlines()
        randomQuote = random.choice(allQuotes)
    print(randomQuote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="talibilahi@yahoo.com",
            msg=f"Subject:Tuesday Motivation\n\n {randomQuote}"
        )


# my_email = "zubairansariinfo941@gmail.com"
# password = "eyfs cdvw kurd lwsk"
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="talibilahi@yahoo.com",
#         msg="Subject:Hello\n\n Hello how are you??"
#     )

# now = dt.datetime.now()
# year = now.year
# month = now.month
# dayOfWeek = now.weekday()
# print(dayOfWeek)
#
# dateOfBirth = dt.datetime(year=1999, month=12, day=11)
# print(dateOfBirth)

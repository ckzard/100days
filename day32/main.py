import smtplib
import datetime as dt
from random import *
import pandas
# make a new text file, with the first line being your email, second line being password, and third line being the app password set up in your gmail account
# update the string after open( on line 5 to reach it

now = dt.datetime.now()
#makes an object called now of class datetime
year = now.year
#which has properties like year which we can access
day_of_week = now.weekday()

birthdays = pandas.read_csv("day32/birthdays.csv")

todays_day = now.day
current_month = now.month

birthday_name = ""
birthday_email = ""
is_birthday = False

for row in birthdays.iterrows():
    if (row[1][3] == current_month and row[1][4] == todays_day):
        birthday_name = row[1][0]
        birthday_email = row[1][1]
        is_birthday = True

if is_birthday == True:

    letter_options = [1, 2, 3];
    letter_choice = choice(letter_options)

    l = open(f"day32/letter_{letter_choice}.txt", "r")
    letter_contents = l.readlines()
    l.close()
    letter_contents[0] = "Hey " + birthday_name + ", \n"
    l = open(f"day32/letter_{letter_choice}.txt", "w")
    letter_string = ""
    for section in letter_contents:
        letter_string += section
    print(letter_string)
    l.write(letter_string)
    l.close()
    # q = open("day32/quotes.txt", 'r', encoding="utf8")
    # quotes = q.readlines()
    # chosen_quote = choice(quotes)
    # q.close()

    l = open(f"day32/letter_{letter_choice}.txt", "r", encoding="utf8")
    letter_contents = l.read()
    l.close()

    gmail_details = []
    f = open("../gmaily.txt", "r")
    for line in f.readlines():
        gmail_details.append(line.strip("\n"))
    f.close()

    my_email = gmail_details[0]
    my_password = gmail_details[1]
    app_pass = gmail_details[2]

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_pass)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_email, msg=f"Subject:Happy Birthday! \n\n {letter_contents}".encode("utf-8"))
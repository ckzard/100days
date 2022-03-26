import smtplib
# make a new text file, with the first line being your email, second line being password, and third line being the app password set up in your gmail account
# update the string after open( on line 5 to reach it
gmail_details = []

f = open("../gmaily.txt", "r")
for line in f.readlines():
    gmail_details.append(line.strip("\n"))

my_email = gmail_details[0]
my_password = gmail_details[1]
app_pass = gmail_details[2]

with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_pass)
    connection.sendmail(from_addr=my_email, to_addrs="chris.burns006@gmail.com", msg="Subject:Hello \n\n This is the body of my email!")
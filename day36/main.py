import requests
from datetime import datetime
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

f = open("../apikeys.txt", "r")
keys = f.readlines()

stock_api_key = keys[0]
news_api_key = keys[1]

today = datetime.now()
current_date = today.date()

## STEP 1: Use https://newsapi.org
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&outputsize=compact&apikey={stock_api_key}'
r = requests.get(stock_url)
stock_data = r.json()["Time Series (Daily)"]

last_2_days = []

count = 0
for item in stock_data.items():
    if count < 2:
        last_2_days.append(item)
        count += 1

day1_close = last_2_days[0][1]["4. close"]
day2_close = last_2_days[1][1]["4. close"]

if float(day1_close) > float(day2_close):
    print("Teslas gone up", last_2_days[0][0], "-", day1_close, "^", last_2_days[1][0], "-", day2_close)
elif float(day1_close) < float(day2_close):
    print("Teslas gone down", last_2_days[0][0], "-", day1_close, "V", last_2_days[1][0], "-", day2_close)
else:
    print("somehow the same")




## STEP 2: Use https://www.alphavantage.co
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
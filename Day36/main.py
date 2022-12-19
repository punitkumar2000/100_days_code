import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

VIRTUAL_TWILIO_NUMBER = "+19787057064"
VERIFIED_NUMBER = "+917876002963"

STOCK_NAME = "IBM"
STOCK_INTERVAL = "5min"

COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "ISHOV10BMCW61DRN"
NEWS_API_KEY = "07c1d60a29ac4d6cb7bda40fa363e949"
TWILIO_SID = "ACd7a4513ac822c8c478da38fc384312bd"
TWILIO_AUTH_TOKEN = "05aa89ab5386eed2b67226d2afb59d20"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": STOCK_INTERVAL,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)

data = response.json()["Time Series (5min)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]

yesterday_closing_price = yesterday_data["4. close"]

# #Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]

day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


# #Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# #Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

# STEP 2: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# #Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# #If difference percentage is greater than 5 then print("Get News").
if abs(diff_percent) == 0:    # should be greater than 0 -- abs(diff_percent) > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

#     #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

#     ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.

#     #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#     #Send each article as a separate message via Twilio.

    proxy_client = TwilioHttpClient()
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)

    # message = client.messages \
    #     .create(
    #     body="It's going to rain today. Remember to bring an ☔️",
    #     from_="+19787057064",
    #     to="+917876002963"
    # )
    # print(message.status)

#     #TODO 8. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=formatted_articles,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
        print(message.status)

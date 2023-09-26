stonks_dictionary = {
    "DOW JONES" : "34,641",
    "S&P 500" : "4,496",
    "NASDAQ" : "14,020",
    "RUSSELL" : "1,880",
    "VIX" : "13.97",
    "TSLA" : "246.49",
    "AAL" : "14.30",
    "MSFT" : "333.55",
    "NXST" : "140.23",
    "AMZN" : "137.27"
}

user_choice = input("Please enter your stonk symbol and I will tell you it's current price: ")

stonk_price = stonks_dictionary.get(user_choice, f"{user_choice} was not found. Please try another stonk symbol")
print(stonk_price)
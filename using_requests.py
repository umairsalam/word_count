import requests

#using requests to pull down web data

url = "https://query1.finance.yahoo.com/v7/finance/download/MU?period1=1525031954&period2=1527623954&interval=1d&events=history&crumb=WLAaf9FVqwT"

url2 = "http://www.umairsalam.com/blog/wp-content/uploads/2018/05/MU.csv"

r = requests.get(url2)
text = r.text

r.close()

print(text)
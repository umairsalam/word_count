import random
import urllib.request

def down_img(url):
    name = random.randrange(1,1000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)

down_img("http://ramadankareemgreetings.com/images/have-a-blessed-ramadan-quotes.jpg")
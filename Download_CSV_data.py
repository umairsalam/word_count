from urllib import request

csv_url = "http://www.umairsalam.com/blog/wp-content/uploads/2018/05/MU.csv"

def down_csv_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    response.close()
    lines = csv_str.split("\\n")
    dest_url = r"csv_data.csv"
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + '\n')
    fx.close()

def down_ssl_csv(csv_url):
    opener = urllib2.build_opener(ConnectHTTPHandler, ConnectHTTPSHandler)
    urllib2.install_opener(opener)
    req = urllib2.Request(csv_url)
    f = urllib2.urlopen(req)
    csv = urllib2.urlopen(req)
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r"csv_data.csv"
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + '\n')
    fx.close()

down_csv_data(csv_url)





from bs4 import BeautifulSoup
# from urllib.request import Request,urlopen
import ssl
import requests
import csv
class scraping:
    def __init__(self):
        # self.urls=["https://www.zomato.com/manali/restaurants?category=2&context=dineout&page="+str(i) for i in range(1,17)]
        # for url in self.urls:
        #     self.scrape(url)
        pass
    def scrape(self,url):
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req=Request(url,headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
        )
        site=urlopen(req).read()
        # proxie={"http": "http://10.10.1.10:3128",
        #    "https": "http://10.10.1.10:1080"}
        # site=requests.get(url,proxies=proxie)
        # print(site)
        soup=BeautifulSoup(site,"html.parser")
        names=[i.text for i in soup.find_all('a',class_="business-name")]
        ph=[i.text for i in soup.find_all('div',class_="phone")]
        add=[i.text for i in soup.find_all('p',class_="adr")]
    def writing(self,name,ph,add):

    
        

s=scraping()
# s.scrape("https://www.zomato.com/manali/restaurants?category=2&context=dineout")
s.scrape("https://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms=Austin%2C+TX")
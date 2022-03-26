import requests
from bs4 import BeautifulSoup

def torob(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser') 

    product_name = soup.find("h1", {"class" : "jsx-2698137455"}).text.strip()
    product_price = soup.find("h2", {"class" : "jsx-2698137455"}).text.replace("از", "").split("تا")

    return {
        'name' : product_name,
        'prices' : {
            'minimum' : product_price[0].strip(),
            'maximum' : product_price[1].strip()
        }
    }
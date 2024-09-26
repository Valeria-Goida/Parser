from bs4 import BeautifulSoup
import requests
import urllib3

def parser():
    urllib3.disable_warnings()
    url = 'https://www.omgtu.ru/news/?SHOWALL_1=1'
    page = requests.get(url, verify=False)
    print(page.status_code)
    soup = BeautifulSoup(page.text,"html.parser")

    block=soup.findAll('a', class_='news-card__link')
    description = ' '
    textfile = open('news.txt', "w+", encoding="utf-8")
    for data in block:
        if data.find('h3'):
            description = data.text
            print(description)
            textfile.write(description)

    textfile.close
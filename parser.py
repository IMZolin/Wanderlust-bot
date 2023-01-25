import requests
from bs4 import BeautifulSoup

# from lxml import etree
from config import URL_LANDMARKS


def GetHTML():
    url = URL_LANDMARKS + '/'
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    req = requests.get(url, headers)
    src = req.text
    print(src)
    with open("index.html", "w", encoding="utf-8") as file:
        file.write(src)
    with open('index.html', 'r', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'html.parser')
    return soup


def GetLandmarks():
    # s = GetHTML()
    with open("index.html", encoding='utf-8') as file:
        src = file.read()
        print("yes")


if __name__ == '__main__':
    # GetHTML()
    GetLandmarks()

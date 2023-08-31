import requests
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
headers = {'User-Agent': user_agent,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


def getHTML(url):
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, "html.parser")


def downloadAudio(word, url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        fileName = f"{word}.mp3"
        with open(fileName, 'wb') as file:
            file.write(response.content)
        return fileName
    return

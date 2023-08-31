import requests
import random
import webrequest
from bs4 import BeautifulSoup


def getExamples(word):
    url = f"https://www.chinesepod.com/dictionary/{word}"
    html = webrequest.getHTML(url)
    divs = html.find_all('div', class_='card sample-sentence-card shadow')

    examples = []
    for div in divs:
        example = div.find("div", class_="simplified-sentence")
        if example:
            examples.append(example.text)

    if (examples):
        formatted = []
        random.shuffle(examples)
        for i, example in enumerate(examples, start=1):
            formatted.append(
                f"{i}: {example.replace(word, '<b>' + word + '</b>')}")
        return "<br>".join(formatted[:5])

    return f"Examples not found for {word}"

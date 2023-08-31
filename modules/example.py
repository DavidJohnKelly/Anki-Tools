import requests
import random
import html
from bs4 import BeautifulSoup


def getExamples(word, html):
    primaryHTML = html.getHTML(f"https://www.iciba.com/word?w={word}")
    examples = primaryHTML.find_all('p', class_='NormalSentence_cn__gyUtC')

    if examples:
        formatted = []
        random.shuffle(examples)
        for i, example in enumerate(examples, start=1):
            formatted.append(
                f"{i}. {example.text.replace(word, '<b>' + word + '</b>')}")
        return "<br>".join(formatted[:5])

    else:
        return f"Examples not found for {word}"

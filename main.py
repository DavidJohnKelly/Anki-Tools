import genanki
from bs4 import BeautifulSoup
from pypinyin import pinyin, Style
import requests

import random
import csv
import os

user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
headers = {'User-Agent': user_agent,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

modelID = random.randrange(1 << 30, 1 << 31)
deckID = random.randrange(1 << 30, 1 << 31)

AnkiModel = genanki.Model(
    modelID,
    'Hanzi Model',
    fields=[
        {'name': 'Character'},
        {'name': 'Pronunciation'},
        {'name': 'Examples'},
        {'name': 'Definition'},
        {'name': 'Pinyin'},
    ],
    templates=[
        {
        'name': 'Card 1',
        'qfmt': 
        """
            <div style="text-align: center;font-size: 20px;">
                {{Character}}
            </div>
        """,
        'afmt': 
        """
            <div style="text-align: center;">
                {{Pronunciation}}
                <hr id="examples">{{Examples}}
                <hr id="definition">{{Definition}}
                <hr id="pinyin">{{Pinyin}}
            </div>
        """,
        },
    ],
)

AnkiDeck = genanki.Deck(
    deckID,
    'Output Deck'
)

AnkiPackage = genanki.Package(AnkiDeck)

def getWords(path):
    words = []
    try:
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                words.extend(row)
    except Exception as e:
        print(f"Error: {e}")
    return words

def downloadAudio(word, url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        fileName = f"{word}.mp3"
        with open(fileName, 'wb') as file:
            file.write(response.content)
        return fileName
    return

def getPronunciation(word):
    url = f"https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define={word}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all("li", class_="entry center_maxed")
    for listElement in elements:
        spanElement = listElement.find("span", class_="word")
        textElements = spanElement.find_all("a", class_=None)
        elementText = ''.join([element.text for element in textElements])
        if(elementText == word):
            iElement = spanElement.find("i", class_= "word_audio fa fa-volume-up")
            audio_url = iElement['data-audio_url']
            file = downloadAudio(word, audio_url)
            if(file):
                AnkiPackage.media_files.append(file)
                return f"[sound:{file}]"
            
    print(f"Failed to download audio for: {word}")
    return ''


def getExamples(word):
    url = f"https://www.iciba.com/word?w={word}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    examples = soup.find_all('p', class_='NormalSentence_cn__gyUtC')

    if examples:
        formatted = []
        random.shuffle(examples)
        for i, example in enumerate(examples, start=1):
            formatted.append(f"{i}. {example.text.replace(word, '<b>' + word + '</b>')}")
        return "<br>".join(formatted[:5])

    else:
        return f"Examples not found for {word}"

def getDefinition(word):
    url = f"https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb={word}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    translation_element = soup.find("div", class_="defs")
    if translation_element:
        return translation_element.get_text()
    else:
        return f"Definition not found for {word}"

def getPinyin(word):
    pinyinList = [pinyin(char, style=Style.TONE, heteronym=True) for char in word]
    return ' '.join(['/ '.join(item) for sublist in pinyinList for item in sublist])


def generateCard(word):
    pronunciation = getPronunciation(word)
    examples = getExamples(word)
    definition = getDefinition(word)
    pinyin = getPinyin(word)

    return genanki.Note(
        model=AnkiModel,
        fields=[word, pronunciation, examples, definition, pinyin]
    )

def main():
    path = input("Enter path of csv file: ")
    words = getWords(path)

    threads = []
    for word in words:
        card = generateCard(word)
        AnkiDeck.add_note(card)

    for thread in threads:
        thread.join()

    AnkiPackage.write_to_file('output.apkg')

    for word in words:
        try:
            os.remove(f"{word}.mp3")
        except FileNotFoundError:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

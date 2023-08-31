# Anki Deck Generator (Mandarin)
## _Generate a formatted anki deck from a list of words_


## Card Features

- Spoken Pronunciation
- Sentence Examples
- English Translations
- Pinyin


## Tech

CSVtoAnki_Mandarin uses a number of open source projects to work properly:

- [Genanki] - library used to export as Anki deck
- [Pypinyin] - backup library to get pinyin pronunciation for words
- [BeautifulSoup] - library used to parse html content
- [Requests] - used to help check whether the provided URL is valid
- [Pydub] - audio library used to aggregate backup audio files
  

## Websites used

- [Yabla] - used for audio files of pronunciation
- [Mdbg] - used for definitions
- [Chinese Pod] - used for pinyin and examples


## Installation

CSVtoAnki_Mandarin requires [Python 3](https://www.python.org/downloads//) v3.11+ to run.

Install the dependencies.

```sh
pip install -r (Path)\requirements.txt
```

## Usage

  1. Compile a csv file of required words
  2. Start run main.py and enter the path to this file
  3. Wait for the script to finish executing
  4. Import the resulting file into Anki


## Notice: Cards are generated at a rate of ~1 per second in order to avoid website bans. Change this at your own risk


## Example
- Input CSV file
![image](https://github.com/DavidJohnKelly/CSVtoAnki_Mandarin/assets/79090791/ebc91129-306c-46af-a8a7-67d18af97404)
- Wait for each card to be generated
![image](https://github.com/DavidJohnKelly/CSVtoAnki_Mandarin/assets/79090791/b68cb145-d9c4-4dad-b97e-44d674a0f694)
- Import resulting deck into Anki
![image](https://github.com/DavidJohnKelly/CSVtoAnki_Mandarin/assets/79090791/2998db15-5c35-4de9-90fb-6c5c61249f0c)

## License

MIT

**Free to use however you want!**

  [Genanki]: <https://github.com/kerrickstaley/genanki>
  [Pypinyin]: <https://github.com/mozillazg/python-pinyin>
  [BeautifulSoup]: <https://github.com/wention/BeautifulSoup4>
  [Requests]: <https://github.com/psf/requests>
  [Pydub]: <https://github.com/jiaaro/pydub>

  [Yabla]: <https://chinese.yabla.com/chinese-english-pinyin-dictionary.php>
  [Mdbg]: <https://www.mdbg.net/chinese/dictionary>
  [Chinese Pod]: <https://www.chinesepod.com/dictionary/>

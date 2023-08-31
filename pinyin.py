from pypinyin import pinyin, Style
import webrequest


def getPinyin(word):
    url = f"https://www.chinesepod.com/dictionary/{word}"
    if (webrequest.validURL(url)):
        html = webrequest.getHTML(url)
        pinyinElement = html.find("div", class_="pinyin")
        if (pinyinElement):
            return pinyinElement.text

    pinyinList = [pinyin(char, style=Style.TONE, heteronym=True)
                  for char in word]
    return ' - '.join(['/ '.join(item) for sublist in pinyinList for item in sublist])

from pypinyin import pinyin, Style


def getPinyin(word, url):
    pinyinList = [pinyin(char, style=Style.TONE, heteronym=True)
                  for char in word]
    return ' '.join(['/ '.join(item) for sublist in pinyinList for item in sublist])

from pydub import AudioSegment
import webrequest


def downloadAudioYabla(word, html):
    elements = html.find_all("li", class_="entry center_maxed")
    for listElement in elements:
        spanElement = listElement.find("span", class_="word")
        textElements = spanElement.find_all("a", class_=None)
        elementText = ''.join([element.text for element in textElements])
        if (elementText == word):
            iElement = spanElement.find(
                "i", class_="word_audio fa fa-volume-up")
            audio_url = iElement['data-audio_url']
            file = webrequest.downloadAudio(word, audio_url)
            return file
    return


def getBackupAudio(word):
    concatenated = AudioSegment.silent(duration=0)
    for character in word:
        print(f"Combining audio for {character}")
        characterHTML = webrequest.getHTML(
            f"https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define={character}")
        backupAudio = downloadAudioYabla(character, characterHTML)
        if (backupAudio):
            audioSegment = AudioSegment.from_mp3(backupAudio)
            concatenated += audioSegment
        else:
            return
    combinedFilePath = f"{word}.mp3"
    concatenated.export(combinedFilePath, format="mp3")
    return combinedFilePath


def getPronunciation(word):
    html = webrequest.getHTML(
        f"https://chinese.yabla.com/chinese-english-pinyin-dictionary.php?define={word}")

    initial = downloadAudioYabla(word, html)
    if (initial):
        return f"[sound:{initial}]"

    backupAudio = getBackupAudio(word)
    if (backupAudio):
        return f"[sound:{backupAudio}]"

    print(f"Failed to download audio for: {word}")
    return ''

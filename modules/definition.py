import html


def getDefinition(word):

    primaryHTML = html.getHTML(f"https://www.chinesepod.com/dictionary/{word}")
    backupHTML = html.getHTML(
        f"https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb={word}")

    translation_element = primaryHTML.find("div", class_="defs")
    if translation_element:
        return translation_element.get_text()

    definitions = []
    backupTranslationDiv = backupHTML.find('div', class_='definition')
    translationList = backupTranslationDiv.find_all(
        "li", class_="list-inline-item")
    for item in translationList:
        definitions.append(item.text)
    if (definitions):
        return "/ ".join(definitions)

    return f"Definition not found for {word}"

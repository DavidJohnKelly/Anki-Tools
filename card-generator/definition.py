import webrequest


def getDefinition(word):
    primaryURL = f"https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb={word}"
    primaryHTML = webrequest.getHTML(primaryURL)

    translation_element = primaryHTML.find("div", class_="defs")
    if translation_element:
        return translation_element.get_text()

    print(f"Definition not found for {word}")
    return f"Definition not found for {word}"

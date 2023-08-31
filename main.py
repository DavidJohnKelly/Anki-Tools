import genanki

import modules.words as words
import modules.card as card
import modules.model as model
import modules.deck as deck

import os

AnkiDeck = deck.generateDeck()
AnkiModel = model.generateModel()
AnkiPackage = genanki.Package(AnkiDeck)


def main():
    path = input("Enter path of csv file: ")
    chineseWords = words.getWords(path)

    for word in chineseWords:
        AnkiCard = card.generateCard(word, AnkiModel)
        if (AnkiCard.fields["Pronunciation"]):
            AnkiPackage.media_files.append(AnkiCard.fields["Pronunciation"])
        AnkiDeck.add_note(AnkiCard)

    AnkiPackage.write_to_file('output.apkg')

    cDir = os.getcwd()
    for filename in os.listdir(cDir):
        if filename.endswith(".mp3"):
            os.remove(os.path.join(cDir, filename))


if __name__ == "__main__":
    main()

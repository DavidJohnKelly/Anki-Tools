import genanki

import words
import card
import deck

import os


AnkiDeck = deck.generateDeck()
AnkiPackage = genanki.Package(AnkiDeck)


def clean():
    cDir = os.getcwd()
    for file in os.listdir(cDir):
        if file.endswith(".mp3"):
            os.remove(os.path.join(cDir, file))


def main():
    path = input("Enter path of csv file: ")
    chineseWords = words.getWords(path)

    for word in chineseWords:
        if word.strip():
            print(f"Word: {word}")
            try:
                AnkiCard = card.generateCard(word)
                audioField = AnkiCard.fields[1]
                if (audioField != ''):
                    audioFile = audioField.split(":")[1][:-1]
                    AnkiPackage.media_files.append(audioFile)
                AnkiDeck.add_note(AnkiCard)
                print(f"Created Card for {word}")
            except:
                print(f"Encountered error when generating card for {word}")

    AnkiPackage.write_to_file('output.apkg')
    print("Finished creating deck")
    clean()


if __name__ == "__main__":
    main()

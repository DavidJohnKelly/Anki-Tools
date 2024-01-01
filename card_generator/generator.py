import os 
import sys
import genanki

import card
import deck

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(parent_dir, 'word_data'))

import learned


AnkiDeck = deck.generateDeck()
AnkiPackage = genanki.Package(AnkiDeck)

learned_words = learned.get_learned_words()


def clean():
    cDir = os.getcwd()
    for file in os.listdir(cDir):
        if file.endswith(".mp3"):
            os.remove(os.path.join(cDir, file))


def generateDeck(words):
    added_words = list()

    for word in words:
        if word not in learned_words and word.strip():
            print(f"Creating Card for '{word}'")
            try:
                AnkiCard = card.generateCard(word)
                audioField = AnkiCard.fields[1]
                if (audioField != ''):
                    audioFile = audioField.split(":")[1][:-1]
                    AnkiPackage.media_files.append(audioFile)
                AnkiDeck.add_note(AnkiCard)
                added_words.append(word)
                print(f"Created Card for '{word}'")
            except Exception as e:
                print(f"When generating card for '{word}' encountered error: {e} ")

    AnkiPackage.write_to_file('output.apkg')
    learned.save_new_words(added_words)
    print("Finished creating deck")
    clean()
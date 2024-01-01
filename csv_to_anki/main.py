import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(parent_dir, 'card_generator'))

import generator
import words


def main():
    path = input("Enter path of csv file: ")
    chineseWords = words.getWords(os.path.abspath(path))
    generator.generateDeck(chineseWords)

if __name__ == "__main__":
    main()

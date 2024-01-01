import os
import sys
import string

import jieba # Used to get the character combinations to make up words

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(parent_dir, 'card_generator'))

import generator

# Function used to check if the string contains chinese characters
# Used to check for dialogue lines
def has_chinese_characters(input_string):
    return any('\u4e00' <= char <= '\u9fff' for char in input_string)


# Return a list of all dialogue lines from the srt file
def get_dialogue(filepath):
    with open(os.path.abspath(filepath), 'r', encoding='utf-8') as file:
        srt_content = file.read()
    lines = srt_content.split('\n')
    dialogue_lines = [line for line in lines if has_chinese_characters(line)]
    return dialogue_lines

# Clean all punctuation, and non character symbols from dialogue
def remove_punctuation(dialogue):
    new_dialogue = list()
    chinese_punctuation = '，。？！；：“”（）【】、《》‘’'
    symbol_list = string.punctuation + chinese_punctuation + '…' + ' '
    translator = str.maketrans('', '', symbol_list)
    for line in dialogue:
        new_dialogue.append(line.translate(translator))
    return new_dialogue

# Use jieba to get all words from the dialogue
def get_dialogue_words(cleaned_dialogue):
    all_words = set()
    for sentence in cleaned_dialogue:
        segmented_words = jieba.cut(sentence)
        unique_words = set(segmented_words)
        all_words.update(unique_words)
    return all_words


def main():
    filepath = input("Enter .srt file path: ")
    dialogue = get_dialogue(filepath)
    cleaned_dialogue = remove_punctuation(dialogue)
    all_words = get_dialogue_words(cleaned_dialogue)
    generator.generateDeck(all_words)


if __name__ == '__main__':
    main()
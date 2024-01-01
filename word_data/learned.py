import csv

file_path = 'word_data/learned_characters.csv'

def get_learned_words():
    learned_words = set()

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        if csvreader.fieldnames:
            for field in csvreader.fieldnames:
                learned_words.add(field)
    return learned_words


def save_new_words(words: list):
    with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(words)
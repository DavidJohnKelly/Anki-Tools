import csv


def getWords(path):
    words = []
    try:
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                words.extend(row)
    except Exception as e:
        print(f"Error: {e}")
    return words

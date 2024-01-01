# Short script to extract all words from an anki .txt deck into a csv file
# Used to update learned_words list from a previous deck
def main():
    file_name = input("Enter the filepath: ")
    # Read the text file and filter out lines starting with #
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if not line.startswith('#')]

    data = []
    for line in lines:
        if line:  # Ignore empty lines
            initial_word = line.split('\t')[0]  # Extract the initial word
            data.append(initial_word)

    # Write the extracted words into a CSV file separated by commas
    with open('word_extractor/extracted.csv', 'w', encoding='utf-8') as output_file:
        for word in data:
            output_file.write(word + ',')
    

if __name__ == '__main__':
    main()
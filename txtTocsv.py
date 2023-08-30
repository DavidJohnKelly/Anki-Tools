import csv
import os
import re

def getCharacters(path):
    characters = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:

                if(line[0] == '#'):
                    pass
                elif(line[0] == '"'):
                    match = re.findall(r'<a .*?>(.*?)</a>', line)
                    if(match):
                        characters.append(''.join(match))
                else:
                    match = re.match(r'^([\u4e00-\u9fff]+)\t', line)
                    if match:
                        characters.append(match.group(1)) 

    except Exception as e:
        print(f"An error occurred: {e}")

    return characters
    

def main():
    path = input("Enter File Name: ")
    characters = getCharacters(path)
    if(characters):
        csv_file = "output.csv"
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(characters)

        print(f"Data written to {csv_file}")
    else:
        print("Error encountered")



    

if __name__ == "__main__":
    main()
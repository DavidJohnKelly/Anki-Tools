import os


def has_chinese_characters(input_string):
    return any('\u4e00' <= char <= '\u9fff' for char in input_string)


def main():
    #filepath = input("Enter .srt file path: ")
    with open(os.path.abspath('80117561_zh-Hans.srt'), 'r', encoding='utf-8') as file:
        srt_content = file.read()
        # Display the content
    lines = srt_content.split('\n')
    dialogue_lines = [line for line in lines if has_chinese_characters(line)]
    print(lines)
    print(dialogue_lines)


if __name__ == '__main__':
    main()
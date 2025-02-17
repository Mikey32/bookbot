def count_words(text_string):
    words = text_string.split()
    return len(words)

def count_characters(text_string):
    char_dict = {}
    lowered_string = text_string.lower()
    for character in lowered_string:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict
def generate_report(old_dict):
    new_dict = {}
    for key in old_dict.keys():
        if key.isalpha():
            new_dict[key] = old_dict[key]
    sort_dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))
    return sort_dict

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        report_file = generate_report(count_characters(file_contents))
        word_count = count_words(file_contents)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    #print(report_file)
    for key, value in report_file.items():
        print(f"The '{key}' character was found {value} times")

main()

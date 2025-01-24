def word_count(string):
    words = string.split()
    return len(words)

def char_count(string):
    chars = {}
    lowered_string = string.lower()
    char_list = list(lowered_string)

    for i in range(0, len(char_list)):
        if char_list[i].isalpha():
            if char_list[i] in chars:
                chars[char_list[i]] += 1
            else:
                chars[char_list[i]] = 1
    
    return chars

def report(string):
    chars = char_count(string)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(string)} words found in the document")
    print("")

    for char, count in chars.items():
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        report(file_contents)

main()
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = 0
        for word in words:
            word_count += 1
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")


def get_letter_quant():
    letter_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower = file_contents.lower()
        for char in lower:
            if char.isalpha():
                if char in letter_count:
                    letter_count[char] += 1
                else:
                    letter_count[char] = 1
    sorted_counts = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_counts:
        print(f"The letter {letter} was used {count} times")
    print("--- end of report ---")


main()
get_letter_quant()

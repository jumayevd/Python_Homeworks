import os
import string
from collections import Counter


FILE_NAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"


def create_file():

    print(f"'{FILE_NAME}' does not exist.")
    content = input("Please enter a paragraph to create the file:\n")
    with open(FILE_NAME, "w") as file:
        file.write(content)
    print(f"File '{FILE_NAME}' created successfully!")


def read_file():
  
    with open(FILE_NAME, "r") as file:
        return file.read()


def count_words(content):

    translator = str.maketrans("", "", string.punctuation)
    words = content.translate(translator).lower().split()
    return Counter(words)


def display_top_words(word_counts, total_words, top_n=5):

    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in word_counts.most_common(top_n):
        print(f"{word} - {count} time{'s' if count > 1 else ''}")


def save_report(word_counts, total_words, top_n=5):
   
    with open(REPORT_FILE, "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write(f"Top {top_n} Words:\n")
        for word, count in word_counts.most_common(top_n):
            report.write(f"{word} - {count}\n")
    print(f"\nReport saved to '{REPORT_FILE}'")


def main():

    if not os.path.exists(FILE_NAME):
        create_file()

 
    content = read_file()
    word_counts = count_words(content)
    total_words = sum(word_counts.values())

   
    top_n = input("How many top common words would you like to see? (default: 5): ").strip()
    top_n = int(top_n) if top_n.isdigit() else 5

   
    display_top_words(word_counts, total_words, top_n)

    save_report(word_counts, total_words, top_n)


if __name__ == "__main__":
    main()

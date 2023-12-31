#!/usr/bin/env python3

import string


# case sensitive
def word_frequencies(filename):
    word_freq = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip(string.punctuation)

                if word:
                    word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


def main():
    frequencies = word_frequencies("src/alice.txt")
    output_file = "output_word_frequencies.txt"
    with open(output_file, "w") as file:
        for word, count in frequencies.items():
            file.write(f"{word}\t{count}\n")


if __name__ == "__main__":
    main()

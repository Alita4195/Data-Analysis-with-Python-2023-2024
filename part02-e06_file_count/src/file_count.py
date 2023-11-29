#!/usr/bin/env python3

import sys


def file_count(filename):
    n_line = 0
    words_num = 0
    char_num = 0
    with open(filename, "r") as new_file:
        for line in new_file:
            words = line.split()
            words_num += len(words)
            char_num += len(line)
            n_line += 1

    return (n_line, words_num, char_num)


def main():
    filenames = sys.argv[1:]
    for filename in filenames:
        n_line, words_num, char_num = file_count(filename)
        print(f"{n_line}\t{words_num}\t{char_num}\t{filename}")


if __name__ == "__main__":
    main()

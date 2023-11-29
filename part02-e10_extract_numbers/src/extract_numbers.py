#!/usr/bin/env python3


def extract_numbers(s):
    digit_set = []
    words = s.split()
    for word in words:
        try:
            num = int(word)  # Try converting to int first
        except ValueError:
            try:
                num = float(word)  # If not an int, try converting to float
            except ValueError:
                continue  # Skip the word if it's not a number
        digit_set.append(num)
    return digit_set


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()

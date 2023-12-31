#!/usr/bin/env python3
import re


def integers_in_brackets(s):
    pattern = r"\[([\s]*[+-]?\d+[\s]*)\]"
    matches = re.findall(pattern, s)

    # Convert the matched strings to integers
    integers = [int(match) for match in matches]

    return integers


def main():
    result = integers_in_brackets(" afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx")
    print(result)


if __name__ == "__main__":
    main()

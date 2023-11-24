#!/usr/bin/env python3

def find_matching(L, pattern):

    return [index for index, item in enumerate(L) if pattern in item]

def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")

if __name__ == "__main__":
    main()


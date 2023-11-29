#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result_list = []
    with open(filename, "r") as new_file:
        for line in new_file:
            pattern = re.search(
                r"(\d+)\s+([a-zA-Z]+)\s+(\d+)\s+(\d+):(\d+).+\s+(.+)", line
            )

            if pattern:
                size, month, day, hour, minute, filename = pattern.groups()
                size = int(size)
                day = int(day)
                hour = int(hour)
                minute = int(minute)
                result_list.append((size, month, day, hour, minute, filename))

    return result_list
    # return pattern


def main():
    results = file_listing("src/listing.txt")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()

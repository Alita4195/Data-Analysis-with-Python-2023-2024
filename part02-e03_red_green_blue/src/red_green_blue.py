#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    colorset = []
    with open(filename, "r") as new_file:
        next(new_file)

        for line in new_file:
            pattern = re.search(r"(\d+)\s+(\d+)\s+(\d+)\s+(.+)", line)
            if pattern:
                red, green, blue, colorname = pattern.groups()
                colorset.append(f"{red}\t{green}\t{blue}\t{colorname.strip()}")

    return colorset
    # with open(filename) as in_file:
    #     l = re.findall(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)\n", in_file.read())
    #     return ["{}\t{}\t{}\t{}".format(r, g, b, name) for r, g, b, name in l]


def main():
    colors = red_green_blue()
    for color in colors:
        print(color)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os
import sys


def file_extensions(filename):
    filenames_without_extension = []
    extension_dict = {}

    with open(filename, "r") as file:
        for line in file:
            file_name = line.strip()
            base_name, file_extension = os.path.splitext(file_name)

            if not file_extension:
                filenames_without_extension.append(base_name)
            else:
                extension = file_extension[1:]  # Remove the preceding period (.)
                if extension not in extension_dict:
                    extension_dict[extension] = []
                extension_dict[extension].append(file_name)

    return filenames_without_extension, extension_dict


def main():
    filename = "src/filenames.txt"
    filenames_without_extension, extension_dict = file_extensions(filename)

    print(f"{len(filenames_without_extension)} files with no extension")

    for extension in sorted(extension_dict.keys()):
        print(f"{extension} {len(extension_dict[extension])}")


if __name__ == "__main__":
    main()

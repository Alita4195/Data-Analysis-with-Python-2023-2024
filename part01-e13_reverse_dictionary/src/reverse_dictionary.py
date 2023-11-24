#!/usr/bin/env python3


def reverse_dictionary(d):
    reversed_dict = {}
    for key, values in d.items():
        for value in values:
            if value in reversed_dict:
                reversed_dict[value].append(key)
            else:
                reversed_dict[value] = [key]
    return reversed_dict
def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reversed_dict = reverse_dictionary(d)
    print(reversed_dict)
if __name__ == "__main__":
    main()

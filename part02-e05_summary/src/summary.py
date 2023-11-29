#!/usr/bin/env python3

import sys
import math


def summary(filename):
    # with open(filename, "r") as new_file:
    #     numbers = [float(line.strip()) for line in new_file]
    with open(filename, "r") as file:
        numbers = []

        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                # Ignore lines that don't represent a number
                continue
    n = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / n
    stddev = math.sqrt(sum((x - average) ** 2 for x in numbers) / (n - 1))

    return total_sum, average, stddev


def main():
    filenames = sys.argv[1:]
    for filename in filenames:
        total_sum, average, stddev = summary(filename)
        print(
            f"File: {filename} Sum: {total_sum:.6f} Average: {average:.6f} Stddev: {stddev:.6f}"
        )


if __name__ == "__main__":
    main()

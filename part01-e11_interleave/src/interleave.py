#!/usr/bin/env python3

def interleave(list1, list2, list3): #（list1, list2, list3）
    result = []
    for items in zip(list1, list2, list3):
        result.extend(items)
        
    return result
def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))


if __name__ == "__main__":
    main()

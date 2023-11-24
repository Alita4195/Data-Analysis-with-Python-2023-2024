#!/usr/bin/env python3

def dice_pairs():
    return [(i, j) for i in range(1, 7) for j in range(1, 7) if i + j == 5]
    
def main():
    
    result = dice_pairs()
    for pair in result:
        print(pair)    

if __name__ == "__main__":
    main()


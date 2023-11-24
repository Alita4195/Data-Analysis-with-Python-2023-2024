#!/usr/bin/env python3

def main():
    for die1 in range(1, 7):  
        for die2 in range(1, 7): 
            if die1 + die2 == 5:  
                print(f"({die1}, {die2})")

if __name__ == "__main__":
    main()

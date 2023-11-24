#!/usr/bin/env python3

def detect_ranges(L):
    L.sort()
    result = []
    start, end = L[0], L[0]
    
    for num in L[1:]:

        if num == end + 1:
            end = num
        else:
            if start == end:
                result.append(start)
            else:
                result.append((start, end + 1)) 
            start, end = num, num
    

    if start == end:
        result.append(start)
    else:
        result.append((start, end + 1))
    
    return result

def main():
    L = [-4, -2, 0, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()

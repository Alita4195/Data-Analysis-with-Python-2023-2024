#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    side1 = 3.0
    side2 = 4.0
    base = 5.0
    height = 6.0

    hyp = triangle.hypotenuse(side1, side2)
    tri_area = triangle.area(base, height)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Donggeun Lim
# Created on: Jan 2019
# This program calculates area of trapezoid.


def caculate_area(base, top, height):
    # calculate area of trapezoid

    # process
    area = base * top * height * 1/2

    return area


def main():
    # input
    base = input("Enter the base of trapezoid (integer): ")
    top = input("Enter the top of trapezoid (integer): ")
    height = input("Enter the height of trapezoid (integer): ")

    # call functions
    try:
        integer_as_base = int(base)
        integer_as_top = int(top)
        integer_as_height = int(height)
        if integer_as_base > 0 and integer_as_height > \
           0 and integer_as_top > 0:
            area = caculate_area(height=integer_as_height,
                                 base=integer_as_base,
                                 top=integer_as_top)
            print("The area of trapezoid is {} m³".format(area))
        else:
            print("Theses number are minus")
    except Exception:
        print("It is not an integer")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Created by: Nathan Araujo
# Created on: Oct 2 2022
# This program shows the scopes of variables


def main():
    # variable definition
    num_of_people = 8
    width = 57.5
    length = 16.9
    my_name_is = "My Name is"
    my_name = " Nathan"

    # using assignment statements
    num_of_people = num_of_people + 3
    area_of_rectangle = length * width
    my_name_final = my_name_is + my_name

    # output
    print("The number of people is {}".format(num_of_people))
    print("The area of a rectangle is {:.2f}".format(area_of_rectangle))
    print(my_name_final)


if __name__ == "__main__":
    main()

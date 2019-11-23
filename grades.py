#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: November 2019
# This program shows the user a grade in a percentage


def calculate(grade):
    # this function calculates the user's grade as a percentage

    # process
    if grade == "4+":
        percentage = 100
    elif grade == "4":
        percentage = 90
    elif grade == "4-":
        percentage = 83
    elif grade == "3+":
        percentage = 78
    elif grade == "3":
        percentage = 75
    elif grade == "3-":
        percentage = 71
    elif grade == "2+":
        percentage = 68
    elif grade == "2":
        percentage = 65
    elif grade == "2-":
        percentage = 61
    elif grade == "1+":
        percentage = 58
    elif grade == "1":
        percentage = 55
    elif grade == "1-":
        percentage = 51
    elif grade == "0+":
        percentage = 45
    elif grade == "0":
        percentage = 35
    elif grade == "0-":
        percentage = 0
    else:
        percentage = -1
    return percentage


def main():
    # this function asks for a grade and outputs the grade in a percentage

    # input
    grade = input("Enter your grade: ")

    # process
    percentage = calculate(grade)

    # output
    if percentage == -1:
        print("")
        print("Please insert a valid grade.")
    else:
        print("")
        print("Your grade is {}%"
              .format(percentage))


if __name__ == "__main__":
    main()

"""
   * Author - Atul Gaikar
   * Date -  05-Nov-2021
   * Time -  5:15 PM
   * Title - Leap Year
"""


def leapYear(year):
    if year < 1000:
        print("Please Enter 4 Digit Year")
        return
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("The given year is a Leap Year")
    else:
        print("The given year is not a Leap Year")


leapYear(int(input("Enter Year: ")))
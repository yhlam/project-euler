"""Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

 - 1 Jan 1900 was a Monday.
 - Thirty days has September,
   April, June and November.
   All the rest have thirty-one,
   Saving February alone,
   Which has twenty-eight, rain or shine.
   And on leap years, twenty-nine.
 - A leap year occurs on any year evenly divisible by 4,
   but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Answer: 171
"""


from datetime import date


def solve():
    LAST_DATE = date(2000, 12, 31)
    count = 0
    current_date = date(1901, 1, 1)

    while current_date < LAST_DATE:
        if current_date.weekday() == 6:
            count += 1

        year = current_date.year
        month = current_date.month

        if month < 12:
            current_date = date(year, month + 1, 1)
        else:
            current_date = date(year + 1, 1, 1)

    return count


if __name__ == '__main__':
    print(solve())

"""Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

Answer: 21124
"""


import math


def solve():
    length = {"1": len("one"),
              "2": len("two"),
              "3": len("three"),
              "4": len("four"),
              "5": len("five"),
              "6": len("six"),
              "7": len("seven"),
              "8": len("eight"),
              "9": len("nine"),
              "10": len("ten"),
              "11": len("eleven"),
              "12": len("twelve"),
              "13": len("thirteen"),
              "14": len("fourteen"),
              "15": len("fifteen"),
              "16": len("sixteen"),
              "17": len("seventeen"),
              "18": len("eighteen"),
              "19": len("nineteen"),
              "20": len("twenty"),
              "30": len("thirty"),
              "40": len("forty"),
              "50": len("fifty"),
              "60": len("sixty"),
              "70": len("seventy"),
              "80": len("eighty"),
              "90": len("ninety"),
              "100": len("hundred"),
              "1000": len("thousand"),
              "and": len("and")}

    sumVal = 0
    for num in range(1, 1001):
        digit = math.trunc(math.log10(num)) + 1

        if digit == 4:
            sumVal += length["1000"]
            sumVal += length[str(num // 1000)]
            num %= 1000
            if num != 0:
                digit = math.trunc(math.log10(num)) + 1
            else:
                digit = 1

        if digit == 3:
            sumVal += length["100"]
            sumVal += length[str(num // 100)]
            num %= 100
            if num != 0:
                sumVal += length["and"]
                if num != 0:
                    digit = math.trunc(math.log10(num)) + 1
                else:
                    digit = 1

        if digit == 2:
            if num < 20:
                sumVal += length[str(num)]
            else:
                sumVal += length[str(math.trunc(num / 10) * 10)]
                num %= 10
                if num != 0:
                    digit = math.trunc(math.log10(num)) + 1
                else:
                    digit = 1

        if digit == 1:
            if num != 0:
                sumVal += length[str(num)]

    return sumVal


if __name__ == '__main__':
    print(solve())

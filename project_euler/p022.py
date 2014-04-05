"""Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order.  Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

Answer: 871198282
"""


def solve():
    def cal_score(name):
        score = 0
        for char in name:
            score += ord(char) - 64
        return score

    nameFile = open('resource/P022_names.txt', 'r')
    names = nameFile.read()
    names = names[1:-1]
    names = names.split('","')
    names.sort()

    score = 0
    size = len(names)
    for i in range(size):
        score += cal_score(names[i]) * (i + 1)
    return score


if __name__ == '__main__':
    print(solve())

import xlrd
import sys

workbook = xlrd.open_workbook('PERMIT.xlsx')

sheet = workbook.sheet_by_index(0)

def getIndex(year):
    vGood = 3
    good = 1.5
    neut = 0
    bad = -1.38
    using = year - 1302 - (12 * (2018 - year))
    other = using - 25
    first = sheet.cell(using, 1)
    second = sheet.cell(other, 1)
    input = ((first.value - second.value) / second.value) / 25

    print("The index in %i was %0.07f" % (year, input))

    if input >= vGood:
        text_file.write("%i: 4\n" % (year))
    elif input >= good and input < vGood:
        text_file.write("%i: 3\n" % (year))
    elif input >= neut and input < good:
        text_file.write("%i: 2\n" % (year))
    elif input >= bad and input < neut:
        text_file.write("%i: 1\n" % (year))
    else:
        text_file.write("%i: 0\n" % (year))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        getIndex(year)
    else:
        text_file = open("bp.txt", "w")
        for i in range(1990, 2019, 1):
            getIndex(i)
        text_file.close()

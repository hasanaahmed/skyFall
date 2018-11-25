import xlrd
import sys

workbook = xlrd.open_workbook('PERMIT.xlsx')

sheet = workbook.sheet_by_index(0)

def getIndex(year):
    vGood = 3
    good = 1.5
    neut = 0
    bad = -1.38
    using = year - 1302
    other = using - 25
    first = sheet.cell(using, 1)
    second = sheet.cell(other, 1)
    input = ((first.value - second.value) / second.value) / 25

    print("The index in %i was %0.07f" % (year, input))

    if input >= vGood:
        return 4
    elif input >= good and input < vGood:
        return 3
    elif input >= neut and input < good:
        return 2
    elif input >= bad and input < neut:
        return 1
    else:
        return 0

if __name__ == '__main__':
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        getIndex(year)
    else:
        getIndex(2018)

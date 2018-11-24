import xlrd
import sys

workbook = xlrd.open_workbook('uedata.xlsx')

sheet = workbook.sheet_by_index(0)

def getIndex(year):
    vGood = sheet.cell(62, 10)
    good = sheet.cell(65, 10)
    neut = sheet.cell(68, 10)
    bad = 3.98
    using = year - 1947
    input = sheet.cell(using, 10)

    print("The rate of UE in %i was %0.07f" % (year, input.value))

    if input.value >= vGood.value:
        return 4
    elif input.value >= good.value and input.value < vGood.value:
        return 3
    elif input.value >= neut.value and input.value < good.value:
        return 2
    elif input.value >= bad and input.value < neut.value:
        return 1
    else:
        return 0

if __name__ == '__main__':
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        getIndex(year)
    else:
        for i in range(2009, 2019, 3):
            getIndex(i)

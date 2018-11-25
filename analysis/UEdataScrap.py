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
        text_file.write("%i: 4\n" % (year))
    elif input.value >= good.value and input.value < vGood.value:
        text_file.write("%i: 3\n" % (year))
    elif input.value >= neut.value and input.value < good.value:
        text_file.write("%i: 2\n" % (year))
    elif input.value >= bad and input.value < neut.value:
        text_file.write("%i: 1\n" % (year))
    else:
        text_file.write("%i: 0\n" % (year))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        getIndex(year)
    else:
        text_file = open("ue.txt", "w")
        for i in range(1990, 2019, 1):
            getIndex(i)
        text_file.close()

import xlrd
import sys

workbook = xlrd.open_workbook('uedata.xlsx')

sheet = workbook.sheet_by_index(0)

def getIndex(year):
    using = year - 1947
    next = using - 30
    firstIn = sheet.cell(using, 10)
    secondIn = sheet.cell(next, 10)
    index = (firstIn.value - secondIn.value) / 29
    print("The index of UE in the %i was %0.07f" % (year, index))
    return(index)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        getIndex(year)
    else:
        for i in range(2009, 2019, 3):
            getIndex(i)

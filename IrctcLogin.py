import xlrd
loc=("D:\\python\\excel\\user_data.xlsx")
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
#print(sheet.ncols)

for i in range(sheet.ncols):
    print(sheet.cell_value(1, i))
import CsV
import openpyxl
csv_data =[]
with open('Sample.csy') as fileobj:
reader scsv.reader(file_obj)for row in reader:
csV_data,append(row)
wb w openpyxl.Workbook()
sheet n wb,active
for row in csv_data:sheet, append(row)
wb.save('Sample.xlsx')
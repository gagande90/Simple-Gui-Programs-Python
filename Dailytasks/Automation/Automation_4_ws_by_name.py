from os.path import dirname, join
import openpyxl                 


excel_doc1 = join(dirname(__file__), 'data', 'TestData1.xlsx')
wb = openpyxl.load_workbook(excel_doc1)

print(wb.sheetnames)
ws2 = wb['DataSheet2']
print(ws2)
print('Active:', wb.active)

 






































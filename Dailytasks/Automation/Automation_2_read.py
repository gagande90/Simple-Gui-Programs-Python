import os
import openpyxl                 


module_dir = os.path.dirname(__file__)
data_folder = os.path.join(module_dir, 'data')
excel_doc1 = os.path.join(data_folder, "TestData1.xlsx") 

wb = openpyxl.load_workbook(excel_doc1)
print(wb)
print(wb.sheetnames)

ws = wb.active
print(ws.title)
ws.title = 'DataSheet1'
print(ws.title)

wb.save(excel_doc1)







































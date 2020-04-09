from os.path import dirname, join
import openpyxl                 


data_folder = join(dirname(__file__), 'data')

for idx in range(1, 6):    
    wb = openpyxl.Workbook()
    doc_name = join(data_folder, 'TestData'+str(idx)+'.xlsx') 
    wb.save(doc_name)




































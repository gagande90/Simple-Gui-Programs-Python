from os.path import dirname, join
import openpyxl                 
from random import randint
from nt import listdir

data_folder = join(dirname(__file__), 'data')

num_of_docs = len(listdir(data_folder))

total = 0

for idx in range(1, num_of_docs + 1):  
    doc_name = join(data_folder, 'TestData'+str(idx)+'.xlsx') 
    wb = openpyxl.load_workbook(doc_name)
    ws = wb.active
    
    for test_idx in range(1, 5):
        cellB = ws.cell(row=test_idx, column=2)
        total += cellB.value
        
print('The Total of all data points collected is:', str(total))































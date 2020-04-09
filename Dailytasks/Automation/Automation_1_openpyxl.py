#-------------------------------------------
# https://openpyxl.readthedocs.io/en/stable/        
#-------------------------------------------

import os
from os.path import join
import openpyxl                 # pip install openpyxl


module_dir = os.path.dirname(__file__)
data_folder = os.path.join(module_dir, 'data')
os.makedirs(data_folder, exist_ok=True)

wb = openpyxl.Workbook()                                # create a new workbook
ws = wb.active                                          # active worksheet
ws['A1'] = 'Data in cell A1'                            # write data into cell
excel_doc1 = join(data_folder, "TestData1.xlsx")        # new file name
wb.save(excel_doc1)                                     # save the workbook

















































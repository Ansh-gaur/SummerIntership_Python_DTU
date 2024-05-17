import openpyxl
import pandas as pd

mylist = [{'ID':'2', 'Quantity':0},{'ID':'2.1','Quantity':0},{'ID':'2.1.1','Quantity':0},{'ID':'2.1.2','Quantity':0},{'ID':'2.1.3','Quantity':94.10902061862528}]
file = 'C://Users//LENOVO//Desktop//data.xlsx'
data = pd.read_excel(file, sheet_name='Sheet1')
workbook = openpyxl.load_workbook(file)
sheet = workbook['Sheet1']
rows = 5
for dictionary in mylist:
    for i in range(0,5):
        if str(data['ID'][i]) == str(dictionary['ID']):
            sheet.cell(row = i+2, column=2).value = dictionary['Quantity']

workbook.save(file)
            




    


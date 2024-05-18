import openpyxl
import pandas as pd

mylist = [{'ID':'2', 'Quantity':0},{'ID':'2.1','Quantity':0},{'ID':'2.1.1','Quantity':0},{'ID':'2.1.2','Quantity':0},{'ID':'2.1.3','Quantity':94.10902061862528}]
file = 'C://Users//LENOVO//Desktop//sample sheet.xlsx'
data = pd.read_excel(file, sheet_name='Sheet 1')
print(data['Unnamed: 1'])
workbook = openpyxl.load_workbook(file)
sheet = workbook['Sheet 1']

for dictionary in mylist:
    for i in range(1,129):
        if str(data['Unnamed: 1'][i]) == str(dictionary['ID']):
            sheet.cell(row = i+2, column=1).value = dictionary['Quantity']

workbook.save(file)




    


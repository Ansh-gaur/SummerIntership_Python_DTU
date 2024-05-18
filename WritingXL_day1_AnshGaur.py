import pandas as p
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook


#INPUT OF LIST OF DICTIONARY
outputFinal=[{'ID':'2.0','Quantity':0},{'ID':'2.1','Quantity':0},{'ID':'2.1.1','Quantity':0},{'ID':'2.1.2','Quantity':0},{'ID':'2.1.3','Quantity':94.10902061862528}]
 


def Find_QTY(ide,L):
    for i in L:
        if i["ID"]==ide:
            return i["Quantity"]

    
path="C:\\Users\\hp\\Desktop\\PythonDTU\\day1.xlsx"     #You can write the path of your file
A=load_workbook(path)
B=A['Sheet1']
t=p.read_excel(path,sheet_name='Sheet1',usecols=("Quantity","ID"))
size=len(t)
for i in range(3,size+3):
    y='A'+str(i)
    rr='B'+str(i)
    B[y]=Find_QTY(B[rr].value,outputFinal)
A.save(path)



   

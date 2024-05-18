import pandas as p
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook


#INPUT OF LIST OF DICTIONARY
outputFinal=[{'ID':'2.0','Quantity':1},{'ID':'2.1','Quantity':2},{'ID':'2.1.1','Quantity':3},{'ID':'2.1.2','Quantity':4},{'ID':'2.1.3','Quantity':5}]
 


def Find_QTY(ide,L):
    for i in L:
        if i["ID"]==ide:
            return i["Quantity"]

    
path="C:\\Users\\hp\\Desktop\\PythonDTU\\sample sheet.xlsx"     #You can write the path of your file
A=load_workbook(path)
B=A['Sheet 1']
t=p.read_excel(path,sheet_name='Sheet 1')
size=len(t)

for i in range(3,132):
    y='A'+str(i)
    rr='B'+str(i)
    print(B[rr].value)
    if(i==3):
        ttt=Find_QTY('2.0',outputFinal)
        if(ttt!=None):
            B[y]=ttt
        else:
            B[y]=B[y].value
    else:
        ttt=Find_QTY(str(B[rr].value),outputFinal)
        if(ttt!=None):
            B[y]=ttt
        else:
            B[y]=B[y].value
A.save(path)


   

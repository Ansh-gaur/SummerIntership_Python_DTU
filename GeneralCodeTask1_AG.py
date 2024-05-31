import pandas as p
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
#INPUT OF LIST OF DICTIONARY
outputFinal=[{'ID':'2','Quantity':1000},{'ID':'2.1','Quantity':2000},{'ID':'2.1.1','Quantity':390},{'ID':'2.1.2','Quantity':0},{'ID':'2.1.3','Quantity':9.45342425}]
def Find_QTY(ide,L):
    for i in L:
        if i["ID"]==ide:
            return i["Quantity"]
path="C:\\Users\\hp\\Desktop\\PythonDTU\\sample sheet.xlsx"     #You can write the path of your file
A=load_workbook(path)
B=A['Sheet 1']
t=p.read_excel(path,sheet_name='Sheet 1')
size=len(t)
#Calculate the row number of header row eg - Here it is (Quantity and ID)
def Row(B):
    i=1
    j='A'
    print(B[(j+str(i))].value)
    while(not B[(j+str(i))].value.isalpha()):
        i+=1
    return i;
i_num=Row(B)

for i in range(i_num+1,size+i_num):
    y='A'+str(i)
    rr='B'+str(i)
    ttt=Find_QTY(str(B[rr].value),outputFinal)
    if(ttt!=None):
        B[y]=ttt
    else:
        B[y]=B[y].value
A.save(path)

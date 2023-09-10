import pandas as pd
#Creating the table for data in dictionary format (Multi row data- pandas data frame)
data={ 'student_number':[12,45,67,89,20],
      'marks_obtained':[89,90,45,67,95],
      'secured class':[1,2,3,4,5]}
table_data=pd.DataFrame(data)
print(table_data)
print("\n")
#Creating the table for data in list (pandas’series)
data=[1,2,3,4,5,6,6,7,8]
series_data=pd.Series(data)
print(series_data)
print("\n")
data_list=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
table_data=pd.DataFrame(data_list)
print(table_data)
print("\n")
#Reading the table and specific row reading
print(table_data.iloc[0])
print("\n")
#Reading the table and specific column reading
print(table_data[0])
print("\n")
#Reading the table and indexing it to extract the data
print(data_list[1][2])
print (table_data.head(2))
print("\n")
print (table_data.tail(1))
print("\n")
data = pd.read_excel("insurance.xlsx")
table_data=pd.DataFrame(data)
print(table_data)









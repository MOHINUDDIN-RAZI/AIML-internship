import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

data = pd.read_excel('multi_linear_Data.xlsx')

df1 = pd.DataFrame(data)
print(df1)
df2 = df1.drop(["Unnamed: 0"],axis = 1)
df2.isnull()
df3 = df2.dropna()
print(df3)
print(df3.duplicated())
df3 = df3.drop_duplicates()
print(df3)
df4=df3.duplicated(subset=['Marks obtained'])
df4 = df3.drop_duplicates(subset=['Marks obtained'],keep='last')
print(df4)
df4.reset_index(inplace=True,drop=True)
print(df4)
plt.scatter(df4['Number of student'],df4['Marks obtained'],color='red')
plt.show()
regr = linear_model.LinearRegression()
x=np.asanyarray(df4['Number of student'])
y = np.asanyarray(df4['Marks obtained'])
print(x)
print(y)
X = x.reshape(-1,1)
print(X)
Y=regr.fit(X,y)
plt.plot(x,regr.predict(X), color = "g")
plt.show()
print("Please enter the number students")
d = int(input('Enter the value'))
b = regr.predict([[d]])[0]
print("Marks scored: {}".format(b))
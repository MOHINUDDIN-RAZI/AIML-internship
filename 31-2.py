import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Load the dataset
df = pd.read_excel("insurance.xlsx")

# Visualize the data
plt.scatter(df['age'], df['charges'], color='red')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.title('Insurance Charges vs Age')
plt.show()

# Prepare the data for linear regression
x = df['age'].values.reshape(-1, 1)  # Feature: Age
y = df['charges'].values             # Target: Charges

# Create a linear regression model
regr = linear_model.LinearRegression()

# Fit the model to the data
regr.fft(x, y)

# Print the coefficient (slope) and intercept of the regression line
print('Coefficient:', regr.coef_)
print('Intercept:', regr.intercept_)
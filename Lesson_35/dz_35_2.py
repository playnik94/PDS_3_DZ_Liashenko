import numpy as np
import pandas as pd

import seaborn as sb
sb.set_style('whitegrid')
import matplotlib.pyplot as plt

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale

from pylab import rcParams
rcParams['figure.figsize'] = 10, 8

from collections import Counter

data = pd.read_csv("petrol1_consumption.csv")
print(data.head())

data.columns = ['Petrol_tax', 'Average_income ', 'Paved_Highways', 'Population_Driver_licence(%)', 'Petrol_Consumption']

datas = data[['Petrol_tax', 'Average_income ','Paved_Highways','Population_Driver_licence(%)']].values
target = data[['Petrol_Consumption']].values
data_names = ['Petrol_Consumption', 'Output']

X, y = scale(datas), target

missing_values = X == np.NAN
print(X[missing_values == True])

LinReg = LinearRegression()

LinReg.fit(X, y)

print(LinReg.score(X, y))

print('intercept: ', LinReg.intercept_)
print('slope: ', LinReg.coef_)

y_pred = LinReg.predict(X)
print('prediction: ', y_pred, sep='\n')

plt.plot(X, y, 'r^')
plt.xlabel('Petrol_Consumption')
plt.ylabel('Output')
plt.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(y,y_pred)
mse = mean_squared_error(y,y_pred)
rmse = np.sqrt(mse)

print(f"Mean_absolute_error{mae:.2f}")
print(f"mean_squared_error{mse:.2f}")
print(f"Root mean squared error{rmse:.2f}")


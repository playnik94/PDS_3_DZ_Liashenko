import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale

from pylab import rcParams
rcParams['figure.figsize'] = 10,8

x = np.array([2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4, 2.7, 4.8, 3.8, 6.9, 7.8]).reshape((-1, 1))
y = np.array([5, 21, 47, 27, 75, 30, 20, 88, 60, 81, 85, 62, 41, 42, 17, 95, 30, 24, 67, 69, 30, 54, 35, 76, 86])

plt.plot(x, y, 'r^')
plt.xlabel('Hours')
plt.ylabel('Scors')
plt.show()

X = x
y = y

LinReg = LinearRegression()
LinReg.fit(X,y)
print(LinReg.intercept_, LinReg.coef_)

print(LinReg.score(X, y))

X_new = np.array([2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4, 2.7, 4.8, 3.8, 6.9, 7.8]).reshape((-1, 1))
X_new
y_new = LinReg.predict(X_new)

plt.plot(X_new, y_new, 'r^')
plt.xlabel('Hours')
plt.ylabel('Scors')
plt.show()
print(LinReg.score(X_new, y_new))

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(y,y_new)
mse = mean_squared_error(y,y_new)
rmse = np.sqrt(mse)

print(f"Mean_absolute_error{mae:.2f}")
print(f"mean_squared_error{mse:.2f}")
print(f"Root mean squared error{rmse:.2f}")



# X = np.array([2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4, 2.7, 4.8, 3.8, 6.9, 7.8]).reshape((-1, 1))
# y = np.array([5, 21, 47, 27, 75, 30, 20, 88, 60, 81, 85, 62, 41, 42, 17, 95, 30, 24, 67, 69, 30, 54, 35, 76, 86])
#
# model = LinearRegression().fit(X, y)
#
# r_sq = model.score(X, y)
# print(f"coefficient of determination: {r_sq}")
#
# print(f"intercept: {model.intercept_}")
#
# print(f"slope: {model.coef_}")
#
# y_pred = model.predict(X)
# print(f"predicted response:\n{y_pred}")
#
# x_new = np.arange(5).reshape((-1, 1))
# print(x_new)
#
# y_new = model.predict(x_new)
# print(y_new)

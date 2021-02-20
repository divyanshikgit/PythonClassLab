import pandas
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np

restaurant_values = pandas.read_csv("data.csv")

x = restaurant_values.drop(['P2', 'City Group', 'Type'], axis=1)
y = restaurant_values["revenue"].astype(str)
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=.33)
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)

# Finding the r2 value
print("R^2 value is: ", model.score(X_test, y_test))

# Finding the RMSE value
predictions = model.predict(X_test)
print("RMSE value is: ", mean_squared_error(y_test, predictions))

# Finding the top 5 correlated features  to the target label
n_features = restaurant_values.select_dtypes(include=[np.number])
corr = n_features.corr()
print('The top 5 correlated features are \n')
print(corr['revenue'].sort_values(ascending=False)[:5], '\n')

# Finding RMSE abd R2 with the top 5 values
x = restaurant_values[['revenue', 'P2', 'P28', 'P6', 'P21']]
y = restaurant_values["revenue"].astype(str)
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=.33)
lr1 = linear_model.LinearRegression()
model = lr1.fit(X_train, y_train)

# Finding the r2 value
print("The new R^2 value is: ", model.score(X_test, y_test))

# Finding the RMSE value
predictions = model.predict(X_test)
print("The new RMSE value is: ", mean_squared_error(y_test, predictions))

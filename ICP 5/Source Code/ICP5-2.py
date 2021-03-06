import pandas
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

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
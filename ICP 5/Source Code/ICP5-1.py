import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

train = pd.read_csv('train.csv')

# To show the outliers
garage_area = train['GarageArea']
sales_price = train['SalePrice']
plt.rcParams['figure.figsize'] = (10, 6)
plt.scatter(garage_area, sales_price, alpha=.5, color='blue')
plt.xlabel('Garage Area')
plt.ylabel('Sale Price')
plt.title('Linear Regression Model')
plt.show()

data_all = pd.concat([train['GarageArea'], train['SalePrice']], axis=1)
z = np.abs(stats.zscore(data_all))
threshold = 5
newtrain = data_all[(z < 5).all(axis=1)]
garage_area = newtrain['GarageArea']
sales_price = newtrain['SalePrice']
plt.rcParams['figure.figsize'] = (10, 6)

# To show without the outliers
plt.scatter(garage_area, sales_price, alpha=.5, color='Red')
plt.xlabel('Garage Area')
plt.ylabel('Sale Price')
plt.title('Linear Regression Model')
plt.show()

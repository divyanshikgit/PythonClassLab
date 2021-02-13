import pandas as pd

train = pd.read_csv('./train.csv')
train["Sex"] = train["Sex"].map({'female': 1, 'male': 0}).astype(int)
print("Correlation between Sex and Survived:", train["Sex"].corr(train["Survived"]))

import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


df = pd.read_csv("glass.csv")
train_x = df.drop("Type", axis=1)
train_y = df["Type"]

train_x, x_test, train_y, y_test = model_selection.train_test_split(train_x, train_y, test_size=0.3, random_state=0)

guassian = GaussianNB()
guassian.fit(train_x, train_y)
y_pred = guassian.predict(x_test)
guassian_score = round(guassian.score(x_test, y_test) * 100, 2)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))


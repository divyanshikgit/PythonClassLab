import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import metrics

df = pd.read_csv("glass.csv")
train_x = df.drop("Type", axis=1)
train_y = df["Type"]

train_x, x_test, train_y, y_test = train_test_split(train_x, train_y, test_size=0.3, random_state=0)

svc = SVC()
svc.fit(train_x, train_y)
y_pred = svc.predict(x_test)
svc_accuracy = round(svc.score(x_test, y_test) * 100, 2)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("SVM Classification Report:\n", classification_report(y_test, y_pred))
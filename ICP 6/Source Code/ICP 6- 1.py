import pandas as pd
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('CC.csv')

#Removing the NULL Values
print(dataset.isnull().sum())

# Checking for null values in each column
dataset = dataset.fillna(dataset.mean())


# Using Elbow method to find the good values to k means
x = dataset.iloc[:, 1:-1]
wcss = []

# Applying K means
for i in range(1, 7):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 7), wcss)
plt.title('With Elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
# To obtain the plot
plt.show()

# To find the Silhouette score for the clusters
nclusters = 4
km = KMeans(n_clusters=nclusters)
km.fit(x)
y_cluster_kmeans = km.predict(x)

# Obtaining the score
score = metrics.silhouette_score(x, y_cluster_kmeans)
print(' The score is', score)

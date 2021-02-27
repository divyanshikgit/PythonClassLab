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

# Removing Null values
print(dataset.isnull().sum())

# checking null values in each column
dataset = dataset.fillna(dataset.mean())

x = dataset.iloc[:, 1:-1]

# Applying Scaling to the data
scaler = StandardScaler()
scaler.fit(x)

# Applying scaling transformation
x_scaler = scaler.transform(x)

# Applying PCA on the data set
pca = PCA(2)
x_pca = pca.fit_transform(x_scaler)

# Finding k means for PCA using elbow
wcss = []
for i in range(1, 7):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(x_pca)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 7), wcss)
plt.title('With Elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

# To find the Silhouette score for the clusters

# The dataframe for PCA
df = pd.DataFrame(data=x_pca, columns=["x", "y"])
nclusters = 3
km = KMeans(n_clusters=nclusters)
km.fit(df)
y_cluster_kmeans = km.predict(df)

# Finding the new silhoutte score
score = metrics.silhouette_score(df, y_cluster_kmeans)
print(' The new score after applying PCA on the dataset is', score)


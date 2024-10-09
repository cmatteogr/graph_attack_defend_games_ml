# Init k-means clustering
#from cuml.cluster import KMeans as KMeans
from sklearn.cluster import KMeans
import torch


print(torch.cuda.is_available())

# Read embedding representation
node2vector_embeddings_filepath = 'node2vector_embeddings.pt'
node2vector_embeddings = torch.load(node2vector_embeddings_filepath)
node2vector_embeddings = node2vector_embeddings.cpu().numpy()


n_clusters = 100  # N Clusters

kmeans_model = KMeans(
    n_clusters=n_clusters,
    max_iter=300,
    tol=1e-4,
    random_state=42
)


kmeans_model.fit(node2vector_embeddings)

labels = kmeans_model.labels_
print(labels)
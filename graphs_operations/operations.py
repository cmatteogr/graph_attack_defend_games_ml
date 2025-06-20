import networkx as nx
from torch_geometric.utils import get_laplacian


def get_betweenness_centrality(G):
    # Calculate betweenness centrality
    betweenness_centrality = nx.betweenness_centrality(G)
    return betweenness_centrality


def get_eigenvector_centrality(G):
    # Calculate eigenvector centrality
    eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)
    return eigenvector_centrality


def get_graph_laplacian(edge_index):
    # Calculate the Laplacian matrix using PyG
    laplacian = get_laplacian(edge_index)
    # Print the Laplacian matrix components
    return laplacian

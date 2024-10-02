import torch
import networkx as nx
from torch_geometric.data import Data
import torch_geometric.transforms as T
from torch_geometric.utils import to_networkx, get_laplacian

from graphs_operations.operations import get_betweenness_centrality, get_eigenvector_centrality, get_laplacian


def test_get_betweenness_centrality(self):
    # Create a simple graph with 5 nodes and edges between them
    # Edges: 0-1, 1-2, 2-3, 3-4, 4-0 (forming a cycle)
    edge_index = torch.tensor([[0, 1, 2, 3, 4, 1, 2, 3, 4, 0],
                               [1, 2, 3, 4, 0, 0, 1, 2, 3, 4]], dtype=torch.long)

    # Create a PyTorch Geometric data object
    data = Data(edge_index=edge_index)

    # Convert to NetworkX graph for centrality calculations
    G = to_networkx(data, to_undirected=True)

    get_betweenness_centrality(G)


def test_eigenvector_centrality(self):
    # Create a simple graph with 5 nodes and edges between them
    # Edges: 0-1, 1-2, 2-3, 3-4, 4-0 (forming a cycle)
    edge_index = torch.tensor([[0, 1, 2, 3, 4, 1, 2, 3, 4, 0],
                               [1, 2, 3, 4, 0, 0, 1, 2, 3, 4]], dtype=torch.long)

    # Create a PyTorch Geometric data object
    data = Data(edge_index=edge_index)

    # Convert to NetworkX graph for centrality calculations
    G = to_networkx(data, to_undirected=True)

    get_eigenvector_centrality(G)


def test_get_betweenness_centrality(self):
    # Create a simple graph with 5 nodes and edges between them
    # Edges: 0-1, 1-2, 2-3, 3-4, 4-0 (forming a cycle)
    edge_index = torch.tensor([[0, 1, 2, 3, 4, 1, 2, 3, 4, 0],
                               [1, 2, 3, 4, 0, 0, 1, 2, 3, 4]], dtype=torch.long)

    get_laplacian(edge_index)

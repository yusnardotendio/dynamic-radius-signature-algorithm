from rdflib import Graph


def load_graph(path: str) -> Graph:
    graph = Graph()
    graph.parse(path)
    return graph
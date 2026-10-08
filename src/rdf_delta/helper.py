from rdflib import BNode, Literal, URIRef
from contextlib import contextmanager
import time


def is_bnode(node) -> bool:
    return isinstance(node, BNode)


def is_literal(node) -> bool:
    return isinstance(node, Literal)


def is_uri(node) -> bool:
    return isinstance(node, URIRef)


def node_to_string(node) -> str:
    return str(node)


def sort_nodes(nodes):
    return sorted(nodes, key=node_to_string)

@contextmanager
def timer(name: str):
    start = time.perf_counter()

    yield

    elapsed = time.perf_counter() - start
    print(f"{name}: {elapsed:.4f}s")
    
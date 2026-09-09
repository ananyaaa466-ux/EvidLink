import networkx as nx


def build_graph(relationships):
    graph = nx.Graph()

    for relationship in relationships:
        graph.add_edge(
            relationship["source"],
            relationship["target"],
            type=relationship["type"],
            timestamp=relationship["timestamp"],
            value=relationship["value"],
            evidence=relationship["evidence"]
        )

    return graph

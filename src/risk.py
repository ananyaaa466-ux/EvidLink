def calculate_risk(graph):
    risk_scores = {}

    for node in graph.nodes():
        score = 0

        connections = graph.degree(node)

        if connections >= 3:
            score += 50
        elif connections == 2:
            score += 25

        risk_scores[node] = score

    return risk_scores
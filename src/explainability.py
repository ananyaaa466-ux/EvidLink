def explain_relationship(relationship):
    return {
        "from": relationship["source"],
        "to": relationship["target"],
        "relationship": relationship["type"],
        "timestamp": relationship["timestamp"],
        "value": relationship["value"],
        "evidence": relationship["evidence"],
        "reason": f"Relationship found through {relationship['evidence']}"
    }

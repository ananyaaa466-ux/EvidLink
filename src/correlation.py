from src.entity_extraction import extract_identifier
def build_relationships(records):
    relationships = []

    for record in records:
        relationship = {
            "source": extract_identifier(record["entity_a"]),
            "target": extract_identifier(record["entity_b"]),
            "type": record["event_type"],
            "timestamp": record["timestamp"],
            "value": record["value"],
            "evidence": record["source"]
        }

        relationships.append(relationship)

    return relationships

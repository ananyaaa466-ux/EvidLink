def identify_entity_type(value):
    if "@upi" in value:
        return "UPI"

    if value.isdigit() and len(value) == 10:
        return "PHONE"

    return "UNKNOWN"


def extract_identifier(value):
    if "@upi" in value:
        return value.split("@")[0]

    return value
def link_entities(value1, value2):
    return extract_identifier(value1) == extract_identifier(value2)
def extract_entities(records):
    entities = set()

    for record in records:
        entities.add(extract_identifier(record["entity_a"]))
        entities.add(extract_identifier(record["entity_b"]))

    return list(entities)
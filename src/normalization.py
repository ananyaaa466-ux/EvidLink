def normalize_cdr(records):
    normalized = []

    for record in records:
        normalized_record = {
            "entity_a": record["caller"],
            "entity_b": record["receiver"],
            "event_type": "call",
            "timestamp": record["timestamp"],
            "value": record["duration_seconds"],
            "source": "cdr.csv"
        }

        normalized.append(normalized_record)

    return normalized


def normalize_upi(records):
    normalized = []

    for record in records:
        normalized_record = {
            "entity_a": record["sender_upi"],
            "entity_b": record["receiver_upi"],
            "event_type": "transaction",
            "timestamp": record["timestamp"],
            "value": record["amount"],
            "source": "upi.csv"
        }

        normalized.append(normalized_record)

    return normalized
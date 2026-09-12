RULES = {
    "Shared IP": {
        "confidence": 60,
        "strength": "MEDIUM",
        "reason": "Both entities were associated with the same IP address"
    },
    "Shared IMEI": {
        "confidence": 96,
        "strength": "STRONG",
        "reason": "Both records contain the same IMEI"
    },
    "Shared IMSI": {
        "confidence": 95,
        "strength": "STRONG",
        "reason": "Both records contain the same IMSI"
    },
    "Repeated UPI Beneficiary": {
        "confidence": 90,
        "strength": "STRONG",
        "reason": "Repeated transactions involve the same UPI beneficiary"
    }
}


def correlate_entities(entity_a, entity_b, relationship_type,
                       evidence_id, record_id):

    rule = RULES[relationship_type]

    return {
        "entity_a": entity_a,
        "entity_b": entity_b,
        "relationship_type": relationship_type,
        "evidence_id": evidence_id,
        "record_id": record_id,
        "confidence": rule["confidence"],
        "strength": rule["strength"],
        "reason": rule["reason"]
    }


relationship = correlate_entities(
    "PHONE-A",
    "PHONE-B",
    "Shared IMEI",
    "EVD-001",
    "#183"
)

print(relationship)
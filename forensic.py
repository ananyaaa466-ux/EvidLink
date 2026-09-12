import hashlib
from datetime import datetime

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


file_path = "test_evidence.txt"

evidence_record = {
    "evidence_id": "EVD-001",
    "filename": file_path,
    "sha256": calculate_sha256(file_path),
    "timestamp": datetime.now().isoformat(),
    "source_type": "Uploaded File"
}

print(evidence_record)
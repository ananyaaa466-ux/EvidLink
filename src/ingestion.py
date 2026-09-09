import csv
import os


def load_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Evidence file not found: {file_path}")

    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)
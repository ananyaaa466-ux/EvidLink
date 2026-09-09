from src.ingestion import load_csv
from src.normalization import normalize_cdr, normalize_upi
from src.correlation import build_relationships
from src.graph import build_graph
from src.risk import calculate_risk
from src.integrity import create_provenance
from src.explainability import explain_relationship


cdr = normalize_cdr(load_csv("data/raw/cdr.csv"))
upi = normalize_upi(load_csv("data/raw/upi.csv"))

relationships = build_relationships(cdr + upi)
graph = build_graph(relationships)

risk_scores = calculate_risk(graph)

print("=== EVIDLINK INVESTIGATION ===")
print("Entities:", graph.number_of_nodes())
print("Relationships:", graph.number_of_edges())
print("Risk Scores:", risk_scores)

print("\n=== EVIDENCE INTEGRITY ===")
print(create_provenance("data/raw/cdr.csv"))
print(create_provenance("data/raw/upi.csv"))

print("\n=== RELATIONSHIP EXAMPLE ===")
print(explain_relationship(relationships[0]))
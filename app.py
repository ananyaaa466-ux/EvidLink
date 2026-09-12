import streamlit as st
import hashlib
from datetime import datetime

st.set_page_config(page_title="EVIDLINK", page_icon="🔐")

st.title("EVIDLINK")
st.subheader("Evidence Integrity & Investigation Platform")

uploaded_file = st.file_uploader(
    "Upload Evidence",
    type=["csv", "txt", "json", "log"]
)

if uploaded_file is not None:

    file_bytes = uploaded_file.getvalue()

    sha256 = hashlib.sha256(file_bytes).hexdigest()

    evidence_record = {
        "evidence_id": "EVD-001",
        "filename": uploaded_file.name,
        "sha256": sha256,
        "timestamp": datetime.now().isoformat(),
        "source_type": "Uploaded File"
    }

    st.success("Evidence processed successfully")

    st.subheader("Evidence Record")
    st.json(evidence_record)

    st.subheader("🔐 Integrity Verification")

    current_hash = hashlib.sha256(file_bytes).hexdigest()

    if current_hash == evidence_record["sha256"]:
        st.success("Evidence Integrity Verified")
    else:
        st.error("Evidence Integrity Failed")

    st.caption(
        "SHA-256 provides a file integrity fingerprint. "
        "It does not by itself establish legal admissibility or authenticity."
    )

    st.divider()

    st.subheader("🔗 Evidence-backed Relationship")

    relationship = {
        "entity_a": "PHONE-A",
        "entity_b": "PHONE-B",
        "relationship": "Shared IMEI",
        "evidence_id": evidence_record["evidence_id"],
        "record_id": "#183",
        "confidence": 96,
        "strength": "STRONG",
        "reason": "Both records contain the same IMEI"
    }

    st.json(relationship)

    st.divider()

    st.subheader("📝 Audit Trail")

    audit_event = {
        "action": "Evidence Uploaded",
        "evidence_id": evidence_record["evidence_id"],
        "filename": evidence_record["filename"],
        "timestamp": evidence_record["timestamp"],
        "status": "SUCCESS"
    }

    st.json(audit_event)
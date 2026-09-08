import streamlit as st

st.set_page_config(
    page_title="EVIDLINK",
    page_icon="🔎",
    layout="wide"
)

st.title("TRACEGRID")
st.subheader("EVIDLINK")
st.write("Explainable Cyber-Fraud Investigation Platform")

st.divider()

st.write("Case #001")


st.subheader("Case Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Case ID", "CASE-001")

with col2:
    st.metric("Priority", "High")

with col3:
    st.metric("Status", "Under Investigation")

st.write("**Case Title:** Suspicious UPI Transaction Network")
st.write("**Lead Investigator:** Shreya")
st.write("**Summary:** Multiple linked UPI transfers have been flagged for possible cyber-fraud activity.")

st.divider()

st.subheader("Investigation Focus")

st.info(
    "Review the linked UPI transfers and identify accounts involved in repeated or unusual transaction patterns."
)

st.subheader("Key Case Signals")

signal1, signal2, signal3 = st.columns(3)

with signal1:
    st.metric("Flagged Transfers", "12")

with signal2:
    st.metric("Linked Accounts", "5")

with signal3:
    st.metric("Risk Level", "High")


    st.subheader("Flagged Transactions")

transactions = [
    {
        "Transaction ID": "TXN-1001",
        "From Account": "Asha Sharma",
        "To Account": "Unknown UPI ID",
        "Amount (₹)": 25000,
        "Risk Flag": "High",
    },
    {
        "Transaction ID": "TXN-1002",
        "From Account": "Ravi Kumar",
        "To Account": "Unknown UPI ID",
        "Amount (₹)": 18000,
        "Risk Flag": "High",
    },
    {
        "Transaction ID": "TXN-1003",
        "From Account": "Asha Sharma",
        "To Account": "Merchant Account",
        "Amount (₹)": 9500,
        "Risk Flag": "Medium",
    },
]

risk_filter = st.selectbox(
    "Filter by risk level",
    ["All", "High", "Medium"]
)

if risk_filter == "All":
    filtered_transactions = transactions
else:
    filtered_transactions = [
        transaction
        for transaction in transactions
        if transaction["Risk Flag"] == risk_filter
    ]
st.dataframe(filtered_transactions, use_container_width=True, hide_index=True)

selected_transaction_id = st.selectbox(
    "Select a transaction to investigate",
    [transaction["Transaction ID"] for transaction in filtered_transactions]
)

selected_transaction = next(
    transaction
    for transaction in filtered_transactions
    if transaction["Transaction ID"] == selected_transaction_id
)

st.write("### Selected Transaction Details")
st.write(f"**From:** {selected_transaction['From Account']}")
st.write(f"**To:** {selected_transaction['To Account']}")
st.write(f"**Amount:** ₹{selected_transaction['Amount (₹)']}")
st.write(f"**Risk Flag:** {selected_transaction['Risk Flag']}")
if selected_transaction["Risk Flag"] == "High":
    st.error(
        "Why flagged: This transfer is linked to an unknown UPI ID and is part of a repeated suspicious transaction pattern."
    )
else:
    st.warning(
        "Why flagged: This transaction needs review because it is connected to an account involved in the case."
    )
if st.button("Mark selected transaction as reviewed"):
    st.success(
        f"{selected_transaction_id} has been marked as reviewed for this investigation session."
    )
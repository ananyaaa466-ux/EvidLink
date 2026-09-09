import streamlit as st

st.set_page_config(
    page_title="EVIDLINK",
    page_icon="🔎",
    layout="wide"
)

if "reviewed_transactions" not in st.session_state:
    st.session_state.reviewed_transactions = []

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
         "Risk Reason": "₹25,000 was sent to an unknown UPI ID linked to repeated transfers.",
    },
    {
        "Transaction ID": "TXN-1002",
        "From Account": "Ravi Kumar",
        "To Account": "Unknown UPI ID",
        "Amount (₹)": 18000,
        "Risk Flag": "High",
           "Risk Reason": "₹18,000 was sent to the same unknown UPI ID from another linked account.",
    },
    {
        "Transaction ID": "TXN-1003",
        "From Account": "Asha Sharma",
        "To Account": "Merchant Account",
        "Amount (₹)": 9500,
        "Risk Flag": "Medium",
          "Risk Reason": "This merchant transfer is connected to an account already involved in the suspicious network.",
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
    st.error(f"Why flagged: {selected_transaction['Risk Reason']}")
else:
    st.warning(f"Why flagged: {selected_transaction['Risk Reason']}")

if st.button("Mark selected transaction as reviewed"):
    if selected_transaction_id not in st.session_state.reviewed_transactions:
        st.session_state.reviewed_transactions.append(selected_transaction_id)

    st.success(
        f"{selected_transaction_id} has been marked as reviewed for this investigation session."
    )

if selected_transaction_id in st.session_state.reviewed_transactions:
    st.write("**Review Status:** Reviewed")
else:
    st.write("**Review Status:** Pending Review")

st.subheader("Evidence Timeline")   

case_timeline = [
    {
        "Time": "09:10 AM",
        "Event": "Suspicious UPI transfer detected",
        "Details": "TXN-1001 sent ₹25,000 to an unknown UPI ID.",
    },
    {
        "Time": "09:18 AM",
        "Event": "Second linked transfer detected",
        "Details": "TXN-1002 sent ₹18,000 to the same unknown UPI ID.",
    },
    {
        "Time": "09:25 AM",
        "Event": "Risk alert generated",
        "Details": "Repeated transfer pattern raised the case risk level to High.",
    },
]

st.dataframe(case_timeline, use_container_width=True, hide_index=True)


st.subheader("Investigator Notes")

investigator_note = st.text_area(
    "Add an observation for the selected transaction",
    placeholder="Example: TXN-1001 should be verified with the bank before further action."
)

if st.button("Save investigation note"):
    if investigator_note.strip():
        st.success("Investigation note saved for this session.")
    else:
        st.warning("Please write a note before saving.")
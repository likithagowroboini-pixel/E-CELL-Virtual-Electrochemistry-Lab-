import streamlit as st

st.title("📝 Electrochemistry Quiz")
questions = [
    ("Oxidation occurs at the:", ["Anode", "Cathode", "Salt bridge", "Voltmeter"], "Anode"),
    ("Reduction occurs at the:", ["Anode", "Cathode", "Salt bridge", "Wire"], "Cathode"),
    ("The sign of ΔG for a spontaneous reaction is:", ["Positive", "Negative", "Zero always", "Cannot be known"], "Negative"),
    ("The formula relating Gibbs energy and cell potential is:", ["ΔG = nFE", "ΔG = −nFE", "ΔG = E/nF", "ΔG = RT ln E"], "ΔG = −nFE"),
]
score = 0
for i, (q, opts, ans) in enumerate(questions, 1):
    choice = st.radio(f"{i}. {q}", opts, key=f"q{i}")
    if choice == ans:
        score += 1

if st.button("Submit Quiz", type="primary"):
    st.success(f"Score: {score}/{len(questions)}")

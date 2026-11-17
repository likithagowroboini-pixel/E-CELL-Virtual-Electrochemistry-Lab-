import streamlit as st
from report_generator import make_report

st.title("📄 Generate Final Report")
st.write("Enter your project details and generate a PDF report from the E-CELL modules.")

name1 = st.text_input("Student 1 name", placeholder="Enter name")
reg1 = st.text_input("Student 1 registration number", placeholder="Enter registration number")
name2 = st.text_input("Student 2 name (optional)", placeholder="Enter name")
reg2 = st.text_input("Student 2 registration number (optional)", placeholder="Enter registration number")

title = st.text_input("Project title", value="E-CELL – Virtual Electrochemistry Lab")
aim = st.text_area("Aim", value="To develop an interactive virtual electrochemistry laboratory for studying galvanic cells, the Nernst equation and Gibbs free energy.")

st.markdown("### Experiment result")
cell = st.text_input("Cell notation", value="Zn | Zn²⁺ || Cu²⁺ | Cu")
e0 = st.number_input("Standard cell potential E° (V)", value=1.10, step=0.01)
observation = st.text_area("Observation", value="The selected Daniell cell produces a positive standard cell potential, indicating spontaneity under standard conditions.")
conclusion = st.text_area("Conclusion", value="The virtual laboratory successfully demonstrates electrochemical cell concepts and provides numerical tools for Nernst and Gibbs free-energy calculations.")

if st.button("Generate PDF Report", type="primary"):
    if not name1:
        st.error("Please enter at least Student 1 name.")
    else:
        pdf = make_report(
            title=title,
            students=[(name1, reg1), (name2, reg2)],
            aim=aim,
            cell=cell,
            e0=e0,
            observation=observation,
            conclusion=conclusion
        )
        st.download_button(
            "⬇️ Download Final Report",
            data=pdf,
            file_name="E-CELL_Virtual_Electrochemistry_Lab_Report.pdf",
            mime="application/pdf"
        )
        st.success("Report generated successfully.")

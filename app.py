import streamlit as st
from calculations import nernst_equation, gibbs_energy, cell_potential

st.set_page_config(page_title="E-CELL Virtual Electrochemistry Lab", page_icon="⚡", layout="wide")

st.markdown("""
<style>
.main-title {
    padding: 28px 30px;
    border-radius: 18px;
    background: linear-gradient(135deg,#0f766e,#164e63);
    color: white;
    margin-bottom: 24px;
}
.card {
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #dbe4ea;
    background: #ffffff;
    box-shadow: 0 4px 14px rgba(0,0,0,.05);
}
.small {color:#64748b;font-size:0.92rem;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("⚡ E-CELL")
st.sidebar.caption("Interactive Engineering Chemistry Learning Lab")
st.sidebar.divider()
st.sidebar.page_link("app.py", label="🏠 Home")
st.sidebar.page_link("pages/1_Galvanic_Cell.py", label="🔋 Galvanic Cell")
st.sidebar.page_link("pages/2_Nernst_Calculator.py", label="🧮 Nernst Calculator")
st.sidebar.page_link("pages/3_Gibbs_Free_Energy.py", label="⚡ Gibbs Free Energy")
st.sidebar.page_link("pages/4_Theory.py", label="📚 Theory")
st.sidebar.page_link("pages/5_Quiz.py", label="📝 Quiz")
st.sidebar.page_link("pages/6_Report.py", label="📄 Generate Report")

st.markdown("""
<div class="main-title">
<h1>⚡ E-CELL</h1>
<p>Virtual Electrochemistry Laboratory</p>
<p>Galvanic Cells • Nernst Equation • Gibbs Free Energy • Theory • Quiz • Report</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Welcome to your virtual chemistry lab")
st.write("Perform electrochemical calculations, explore a galvanic cell, test your knowledge, and generate a structured experiment report.")

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><h3>🔋 Galvanic Cell</h3><p>Identify anode, cathode, electron flow and cell notation.</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h3>🧮 Nernst Equation</h3><p>Calculate cell potential under non-standard conditions.</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><h3>⚡ Gibbs Energy</h3><p>Connect cell potential with spontaneity and ΔG.</p></div>', unsafe_allow_html=True)

st.markdown("### Quick Start")
st.info("Start with **Galvanic Cell**, then use the **Nernst Calculator** and **Gibbs Free Energy** modules. Finish with **Generate Report**.")

st.markdown("### Built-in example: Daniell Cell")
st.code("Zn | Zn²⁺ || Cu²⁺ | Cu", language="text")
st.write("For the standard Daniell cell, E°cell = E°cathode − E°anode. The standard reaction is spontaneous when E°cell is positive.")

import streamlit as st
from calculations import nernst_equation

st.title("🧮 Nernst Equation Calculator")
st.latex(r"E = E^\circ - \frac{RT}{nF}\ln Q")

st.write("Calculate the electrode/cell potential at a chosen temperature and reaction quotient.")

c1, c2 = st.columns(2)
with c1:
    e0 = st.number_input("E° (V)", value=1.10, step=0.01, format="%.4f")
    n = st.number_input("Number of electrons, n", min_value=1, value=2, step=1)
with c2:
    q = st.number_input("Reaction quotient, Q", min_value=0.000001, value=1.0, step=0.1, format="%.6f")
    temp = st.number_input("Temperature (K)", min_value=1.0, value=298.15, step=1.0)

if st.button("Calculate E", type="primary"):
    e = nernst_equation(e0, n, q, temp)
    st.success(f"Cell potential = {e:.4f} V")
    st.caption("Equation used: E = E° − (RT/nF) ln Q")

import streamlit as st
from calculations import gibbs_energy

st.title("⚡ Gibbs Free Energy Calculator")
st.latex(r"\Delta G = -nFE")

n = st.number_input("Number of electrons transferred, n", min_value=1, value=2, step=1)
e = st.number_input("Cell potential, E (V)", value=1.10, step=0.01, format="%.4f")

if st.button("Calculate ΔG", type="primary"):
    dg = gibbs_energy(n, e)
    st.success(f"ΔG = {dg:.2f} J mol⁻¹")
    st.write(f"or ΔG = {dg/1000:.3f} kJ mol⁻¹")
    if dg < 0:
        st.info("ΔG is negative, so the reaction is thermodynamically spontaneous under the stated conditions.")
    elif dg > 0:
        st.warning("ΔG is positive, so the reaction is non-spontaneous in the stated direction.")
    else:
        st.info("ΔG = 0 indicates equilibrium.")

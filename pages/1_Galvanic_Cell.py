import streamlit as st
from calculations import cell_potential

st.title("🔋 Galvanic Cell Simulator")
st.write("Explore a simple electrochemical cell and identify its important components.")

metals = {
    "Zn / Zn²⁺": -0.76,
    "Cu / Cu²⁺": 0.34,
    "Fe / Fe²⁺": -0.44,
    "Ag / Ag⁺": 0.80,
    "Mg / Mg²⁺": -2.37,
    "Ni / Ni²⁺": -0.25,
}

left, right = st.columns(2)
with left:
    anode = st.selectbox("Choose anode half-cell", list(metals.keys()), index=0)
with right:
    cathode = st.selectbox("Choose cathode half-cell", list(metals.keys()), index=1)

if anode == cathode:
    st.warning("Choose two different half-cells.")
    st.stop()

ea = metals[anode]
ec = metals[cathode]
e = cell_potential(ec, ea)

st.markdown("### Cell analysis")
c1, c2, c3 = st.columns(3)
c1.metric("Anode", anode)
c2.metric("Cathode", cathode)
c3.metric("E°cell", f"{e:.3f} V")

if e > 0:
    st.success("The selected combination gives a positive E°cell, indicating a spontaneous galvanic reaction under standard conditions.")
else:
    st.error("The selected direction is not spontaneous under standard conditions. Swap the half-cells.")

st.markdown("### Electron flow")
st.write(f"Electrons flow from **{anode}** (anode) → **{cathode}** (cathode) when E°cell is positive.")

st.markdown("### Cell notation")
def strip_name(x):
    return x.replace(" / ", " | ")
st.code(f"{strip_name(anode)} || {strip_name(cathode)}", language="text")

st.markdown("### Half-cell potentials")
st.table({
    "Half-cell": [anode, cathode],
    "Standard reduction potential (V)": [ea, ec]
})

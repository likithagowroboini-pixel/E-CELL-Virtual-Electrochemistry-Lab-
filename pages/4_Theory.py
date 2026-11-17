import streamlit as st

st.title("📚 Theory")
topics = {
"Galvanic Cell": """A galvanic (voltaic) cell converts chemical energy into electrical energy through a spontaneous redox reaction. Oxidation occurs at the anode and reduction occurs at the cathode.""",
"Nernst Equation": """The Nernst equation relates electrode/cell potential to the standard potential, temperature, number of electrons and reaction quotient.""",
"Gibbs Free Energy": """The relationship ΔG = −nFE connects electrochemical potential with thermodynamic spontaneity.""",
"Cell Notation": """A common representation is anode | anode ion || cathode ion | cathode. The double line represents the salt bridge or junction."""
}
for name, text in topics.items():
    with st.expander(name, expanded=(name=="Galvanic Cell")):
        st.write(text)

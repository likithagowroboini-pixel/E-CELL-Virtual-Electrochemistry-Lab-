import math

def cell_potential(cathode_e, anode_e):
    return cathode_e - anode_e

def nernst_equation(e0, n, q, temperature=298.15):
    # E = E° - (RT/nF) ln Q
    R = 8.314462618
    F = 96485.33212
    if n <= 0:
        raise ValueError("Number of electrons n must be positive.")
    if q <= 0:
        raise ValueError("Reaction quotient Q must be positive.")
    return e0 - (R * temperature / (n * F)) * math.log(q)

def gibbs_energy(n, ecell):
    # ΔG = -nFE
    F = 96485.33212
    return -n * F * ecell


def maillard_reaction(A, E_a, T):
    import numpy as np
    R = 8.314  # J/(mol·K)
    return A * np.exp(-E_a / (R * T))

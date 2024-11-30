
def heat_and_moisture_transfer(T_initial, k, t, dx, dy):
    import numpy as np
    T_initial = np.array(T_initial)
    nx, ny = T_initial.shape
    T = T_initial.copy()
    for _ in range(t):
        T[1:-1, 1:-1] = T[1:-1, 1:-1] + k * (
            (T[2:, 1:-1] - 2*T[1:-1, 1:-1] + T[:-2, 1:-1]) / dx**2 +
            (T[1:-1, 2:] - 2*T[1:-1, 1:-1] + T[1:-1, :-2]) / dy**2
        )
    return T


import os
from models.heat_transfer import heat_and_moisture_transfer
from models.maillard import maillard_reaction

def main():
    print("Cooking Simulation Project")
    # Example: Heat Transfer Simulation
    T_initial = [[100]*10 for _ in range(10)]  # Example 10x10 grid
    k = 0.01
    result = heat_and_moisture_transfer(T_initial, k, t=100, dx=1, dy=1)
    print("Heat Transfer Simulation Complete. Results saved in outputs/")

if __name__ == "__main__":
    main()

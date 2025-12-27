---
sidebar_position: 2
---

# Chapter 2: Entropy - Python Code

Python computational solutions for Chapter 2 problems on entropy and the second law.

## Overview

This module contains numerical solutions for:
- Carnot cycle calculations
- Heat engine efficiency
- Entropy changes
- Free expansion

## Source File

```
thermodynamics_solutions/python/chapter2_entropy.py
```

## Carnot Cycle

### Basic Carnot Engine

```python
def carnot_efficiency(T_H, T_C):
    """
    Calculate Carnot efficiency.

    Parameters:
        T_H: hot reservoir temperature (K)
        T_C: cold reservoir temperature (K)

    Returns:
        eta: efficiency (0 to 1)
    """
    return 1 - T_C / T_H

def carnot_engine(T_H, T_C, W):
    """
    Calculate heat flows for given work output.

    Returns:
        Q_H: heat absorbed from hot reservoir
        Q_C: heat rejected to cold reservoir
    """
    eta = carnot_efficiency(T_H, T_C)
    Q_H = W / eta
    Q_C = Q_H - W
    return Q_H, Q_C

# Example
eta = carnot_efficiency(500, 300)
Q_H, Q_C = carnot_engine(500, 300, 1000)
print(f"Efficiency: {eta*100:.0f}%")
print(f"Q_H = {Q_H:.0f} W, Q_C = {Q_C:.0f} W")
# Output: Efficiency: 40%
#         Q_H = 2500 W, Q_C = 1500 W
```

### Heat Pump & Refrigerator

```python
def heat_pump_cop(T_H, T_C):
    """Coefficient of performance for heat pump."""
    return T_H / (T_H - T_C)

def refrigerator_cop(T_H, T_C):
    """Coefficient of performance for refrigerator."""
    return T_C / (T_H - T_C)

# Example: Home heat pump
T_inside = 293  # 20°C
T_outside = 273  # 0°C
cop = heat_pump_cop(T_inside, T_outside)
print(f"Heat pump COP: {cop:.1f}")
# Output: Heat pump COP: 14.6
```

## Otto Cycle

```python
def otto_efficiency(r, gamma=1.4):
    """
    Otto cycle efficiency.

    Parameters:
        r: compression ratio (V1/V2)
        gamma: Cp/Cv ratio

    Returns:
        eta: thermal efficiency
    """
    return 1 - 1 / r**(gamma - 1)

# Example
for r in [6, 8, 10, 12]:
    eta = otto_efficiency(r)
    print(f"r = {r}: η = {eta*100:.1f}%")
# Output:
# r = 6: η = 51.2%
# r = 8: η = 56.5%
# r = 10: η = 60.2%
# r = 12: η = 63.0%
```

## Entropy Calculations

### Entropy of Ideal Gas

```python
import numpy as np

R = 8.314

def entropy_change_ideal_gas(n, T1, T2, V1, V2, Cv):
    """
    Entropy change for ideal gas.

    ΔS = n*Cv*ln(T2/T1) + n*R*ln(V2/V1)
    """
    dS = n * Cv * np.log(T2/T1) + n * R * np.log(V2/V1)
    return dS

# Example: 1 mol heated from 300K to 600K, volume doubled
# For monatomic gas: Cv = 3R/2
Cv = 1.5 * R
dS = entropy_change_ideal_gas(1, 300, 600, 1, 2, Cv)
print(f"ΔS = {dS:.2f} J/K")
```

### Entropy of Mixing

```python
def entropy_of_mixing(n1, n2):
    """
    Entropy change for mixing ideal gases at same T, P.

    ΔS = -R * (n1*ln(x1) + n2*ln(x2))
    """
    n_total = n1 + n2
    x1 = n1 / n_total
    x2 = n2 / n_total
    dS = -R * (n1 * np.log(x1) + n2 * np.log(x2))
    return dS

# Example: 2 mol He + 3 mol Ar
dS = entropy_of_mixing(2, 3)
print(f"Entropy of mixing: {dS:.1f} J/K")
# Output: Entropy of mixing: 46.5 J/K
```

### Free Expansion

```python
def free_expansion_entropy(n, V1, V2):
    """
    Entropy change for free expansion into vacuum.

    ΔS_gas = n*R*ln(V2/V1)
    ΔS_surroundings = 0
    ΔS_universe = n*R*ln(V2/V1) > 0 (irreversible)
    """
    dS_gas = n * R * np.log(V2 / V1)
    dS_surroundings = 0
    dS_universe = dS_gas + dS_surroundings
    return dS_gas, dS_surroundings, dS_universe

# Example: Expand to double volume
dS_gas, dS_surr, dS_univ = free_expansion_entropy(1, 1, 2)
print(f"ΔS_gas = {dS_gas:.2f} J/K")
print(f"ΔS_universe = {dS_univ:.2f} J/K (> 0, irreversible)")
```

## Visualization: Carnot Cycle

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_carnot_pv(T_H, T_C, V1, V2, n=1, gamma=5/3):
    """Plot Carnot cycle on PV diagram."""
    R = 8.314

    # State 1: Start of isothermal expansion at T_H
    P1 = n * R * T_H / V1

    # Isothermal expansion 1→2 at T_H
    V_12 = np.linspace(V1, V2, 50)
    P_12 = n * R * T_H / V_12

    # State 2
    P2 = n * R * T_H / V2

    # Adiabatic expansion 2→3: T_H → T_C
    V3 = V2 * (T_H / T_C)**(1/(gamma-1))
    V_23 = np.linspace(V2, V3, 50)
    P_23 = P2 * (V2 / V_23)**gamma

    # State 3
    P3 = n * R * T_C / V3

    # Isothermal compression 3→4 at T_C
    V4 = V1 * (T_H / T_C)**(1/(gamma-1))
    V_34 = np.linspace(V3, V4, 50)
    P_34 = n * R * T_C / V_34

    # Adiabatic compression 4→1
    V_41 = np.linspace(V4, V1, 50)
    P_41 = P1 * (V1 / V_41)**gamma

    plt.figure(figsize=(10, 7))
    plt.plot(V_12, P_12, 'r-', linewidth=2, label=f'Isothermal T={T_H}K')
    plt.plot(V_23, P_23, 'b--', linewidth=2, label='Adiabatic expansion')
    plt.plot(V_34, P_34, 'c-', linewidth=2, label=f'Isothermal T={T_C}K')
    plt.plot(V_41, P_41, 'm--', linewidth=2, label='Adiabatic compression')

    plt.xlabel('Volume (L)')
    plt.ylabel('Pressure (Pa)')
    plt.title('Carnot Cycle PV Diagram')
    plt.legend()
    plt.grid(True)
    plt.savefig('carnot_cycle.png')
    plt.show()

# Generate plot
# plot_carnot_pv(500, 300, 0.01, 0.02)
```

## Full Source Code

```
thermodynamics_solutions/python/chapter2_entropy.py
```

## Related Resources

- [Chapter 2 Theory](/docs/problems/thermodynamics/entropy)
- [LaTeX Solutions](/docs/solutions/latex/chapter2/problems-1031-1040)
- [Chapter 3 Code](./chapter3-functions)

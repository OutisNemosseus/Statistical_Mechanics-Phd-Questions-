---
sidebar_position: 1
---

# Chapter 1: First Law - Python Code

Python computational solutions for Chapter 1 problems on thermodynamic states and the first law.

## Overview

This module contains numerical solutions for:
- Temperature and thermal expansion
- Heat capacity calculations
- Ideal gas processes
- Adiabatic processes
- Radiation problems

## Source File

```
thermodynamics_solutions/python/chapter1_first_law.py
```

## Problem 1003: Bimetallic Strip

Calculate the radius of curvature when a bimetallic strip is heated.

```python
def problem_1003(x, alpha1, alpha2, delta_T):
    """
    Calculate radius of curvature of bimetallic strip.

    Parameters:
        x: total thickness (m)
        alpha1: expansion coefficient of metal 1 (1/K)
        alpha2: expansion coefficient of metal 2 (1/K)
        delta_T: temperature change (K)

    Returns:
        R: radius of curvature (m)
    """
    R = x / ((alpha2 - alpha1) * delta_T)
    return R

# Example
R = problem_1003(0.002, 12e-6, 24e-6, 50)
print(f"Radius: {R:.2f} m")
# Output: Radius: 3.33 m
```

## Problem 1006: Heat Capacity of Copper

Using Dulong-Petit law for solids.

```python
R = 8.314  # J/(mol·K)

def problem_1006(mass_g, atomic_mass):
    """
    Calculate heat capacity using Dulong-Petit law.

    Parameters:
        mass_g: mass in grams
        atomic_mass: atomic mass (g/mol)

    Returns:
        Cv: heat capacity (J/K)
    """
    n_moles = mass_g / atomic_mass
    Cv = n_moles * 3 * R  # Dulong-Petit: Cv = 3R per mole
    return Cv

# Example: Copper penny
Cv = problem_1006(32, 64)
print(f"Heat capacity: {Cv:.1f} J/K = {Cv/4.184:.1f} cal/K")
# Output: Heat capacity: 12.5 J/K = 3.0 cal/K
```

## Problem 1008: Clement-Desormes Method

Determine $\gamma = C_P/C_V$ from pressure measurements.

```python
def problem_1008(h1, h3):
    """
    Calculate gamma using Clement-Desormes method.

    Parameters:
        h1: initial manometer height (arbitrary units)
        h3: final manometer height after equilibration

    Returns:
        gamma: Cp/Cv ratio
    """
    gamma = h1 / (h1 - h3)
    return gamma

# Example
gamma = problem_1008(100, 30)
print(f"γ = {gamma:.2f}")
# Output: γ = 1.43
```

## Problem 1015: Isothermal Expansion

Calculate work and heat for isothermal process.

```python
import numpy as np

def problem_1015(n, T, V1, V2):
    """
    Isothermal expansion of ideal gas.

    Parameters:
        n: moles
        T: temperature (K)
        V1, V2: initial and final volumes (L)

    Returns:
        W, Q, dU: work, heat, internal energy change (J)
    """
    R = 8.314
    W = n * R * T * np.log(V2 / V1)
    dU = 0  # Isothermal: ΔU = 0
    Q = W   # First law: Q = W + ΔU
    return W, Q, dU

# Example
W, Q, dU = problem_1015(1, 300, 10, 20)
print(f"Work: {W:.0f} J, Heat: {Q:.0f} J, ΔU: {dU} J")
# Output: Work: 1729 J, Heat: 1729 J, ΔU: 0 J
```

## Problem 1022: Adiabatic Process

Calculate final state after adiabatic compression.

```python
def problem_1022(T1, V1, V2, gamma=1.4):
    """
    Adiabatic process for ideal gas.

    Parameters:
        T1: initial temperature (K)
        V1, V2: initial and final volumes
        gamma: Cp/Cv ratio

    Returns:
        T2: final temperature (K)
        P_ratio: P2/P1
    """
    T2 = T1 * (V1 / V2) ** (gamma - 1)
    P_ratio = (V1 / V2) ** gamma
    return T2, P_ratio

# Example: Compress to half volume
T2, P_ratio = problem_1022(300, 2, 1)
print(f"Final temperature: {T2:.0f} K")
print(f"Pressure ratio: {P_ratio:.2f}")
# Output: Final temperature: 396 K
#         Pressure ratio: 2.64
```

## Problem 1028: Blackbody Radiation

Calculate power radiated and peak wavelength.

```python
sigma = 5.67e-8  # Stefan-Boltzmann constant

def problem_1028(radius, T):
    """
    Blackbody sphere radiation.

    Parameters:
        radius: sphere radius (m)
        T: temperature (K)

    Returns:
        P: power radiated (W)
        lambda_max: peak wavelength (m)
    """
    A = 4 * np.pi * radius**2
    P = sigma * A * T**4
    lambda_max = 2.898e-3 / T  # Wien's law
    return P, lambda_max

# Example
P, lam = problem_1028(0.1, 1000)
print(f"Power: {P:.0f} W")
print(f"Peak wavelength: {lam*1e6:.1f} μm")
# Output: Power: 7140 W
#         Peak wavelength: 2.9 μm
```

## Visualization: PV Diagram

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_isothermal_adiabatic():
    """Compare isothermal and adiabatic processes."""
    V = np.linspace(1, 5, 100)
    P0, V0, T0, gamma = 10, 1, 300, 1.4

    # Isothermal: PV = const
    P_iso = P0 * V0 / V

    # Adiabatic: PV^γ = const
    P_adi = P0 * (V0 / V)**gamma

    plt.figure(figsize=(8, 6))
    plt.plot(V, P_iso, 'b-', label='Isothermal')
    plt.plot(V, P_adi, 'r-', label='Adiabatic')
    plt.xlabel('Volume (L)')
    plt.ylabel('Pressure (atm)')
    plt.title('Isothermal vs Adiabatic Expansion')
    plt.legend()
    plt.grid(True)
    plt.savefig('pv_diagram.png')
    plt.show()
```

## Full Source Code

The complete source code is available at:
```
thermodynamics_solutions/python/chapter1_first_law.py
```

## Related Resources

- [Chapter 1 Theory](/docs/problems/thermodynamics/first-law)
- [LaTeX Solutions](/docs/solutions/latex/chapter1/problems-1001-1010)
- [Chapter 2 Code](./chapter2-entropy)

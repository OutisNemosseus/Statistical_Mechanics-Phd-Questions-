---
sidebar_position: 3
---

# Chapter 3: Functions - Python Code

Python computational solutions for Chapter 3 problems on thermodynamic potentials and phase transitions.

## Overview

This module contains numerical solutions for:
- Maxwell relations verification
- Clausius-Clapeyron calculations
- Phase diagrams
- Atmospheric thermodynamics

## Source File

```
thermodynamics_solutions/python/chapter3_functions.py
```

## Thermodynamic Potentials

### Van der Waals Gas Properties

```python
import numpy as np

R = 8.314  # J/(mol·K)

def vdw_pressure(V, T, n=1, a=0.1408, b=3.913e-5):
    """
    Van der Waals equation of state.

    P = nRT/(V-nb) - a*n²/V²

    Parameters:
        V: volume (m³)
        T: temperature (K)
        n: moles
        a, b: van der Waals constants (default: N₂)
    """
    return n * R * T / (V - n * b) - a * n**2 / V**2

def vdw_internal_energy_change(V1, V2, n=1, a=0.1408):
    """
    Internal energy change for van der Waals gas.

    (∂U/∂V)_T = a/V² for van der Waals
    ΔU = a*(1/V1 - 1/V2)
    """
    return n**2 * a * (1/V1 - 1/V2)
```

### $C_P - C_V$ Calculation

```python
def cp_minus_cv_ideal(n):
    """For ideal gas: Cp - Cv = nR"""
    return n * R

def cp_minus_cv_general(T, V, alpha, kappa_T):
    """
    General formula: Cp - Cv = T*V*α²/κ_T

    Parameters:
        T: temperature (K)
        V: volume (m³)
        alpha: thermal expansion coefficient (1/K)
        kappa_T: isothermal compressibility (1/Pa)
    """
    return T * V * alpha**2 / kappa_T

# Example: Copper at room temperature
T = 300
V = 7.1e-6  # molar volume m³/mol
alpha = 49e-6  # 1/K
kappa_T = 7.2e-12  # 1/Pa
diff = cp_minus_cv_general(T, V, alpha, kappa_T)
print(f"Cp - Cv for Cu: {diff:.2f} J/(mol·K)")
```

## Clausius-Clapeyron Equation

### Vapor Pressure Calculation

```python
def vapor_pressure(T, T_ref, P_ref, L, M):
    """
    Calculate vapor pressure using Clausius-Clapeyron.

    ln(P/P_ref) = -(L*M/R)*(1/T - 1/T_ref)

    Parameters:
        T: temperature (K)
        T_ref: reference temperature (K)
        P_ref: vapor pressure at T_ref (Pa)
        L: latent heat (J/kg)
        M: molar mass (kg/mol)
    """
    exponent = -(L * M / R) * (1/T - 1/T_ref)
    return P_ref * np.exp(exponent)

# Example: Water vapor pressure
T_boil = 373.15  # 100°C
P_atm = 101325   # Pa
L_vap = 2.26e6   # J/kg
M_water = 0.018  # kg/mol

# Pressure at 90°C
T = 363.15
P = vapor_pressure(T, T_boil, P_atm, L_vap, M_water)
print(f"Vapor pressure at 90°C: {P/1000:.1f} kPa")
# Output: Vapor pressure at 90°C: 70.1 kPa
```

### Boiling Point Calculation

```python
from scipy.optimize import fsolve

def boiling_point(P, T_ref, P_ref, L, M):
    """Find boiling temperature at given pressure."""
    def equation(T):
        return vapor_pressure(T, T_ref, P_ref, L, M) - P

    T_guess = T_ref * (P / P_ref)**0.1  # Initial guess
    T_boil = fsolve(equation, T_guess)[0]
    return T_boil

# Example: Boiling point at half atmosphere
T = boiling_point(P_atm/2, T_boil, P_atm, L_vap, M_water)
print(f"Boiling point at 0.5 atm: {T-273.15:.1f}°C")
# Output: Boiling point at 0.5 atm: 81.6°C
```

## Phase Diagram

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_water_phase_diagram():
    """Plot simplified water phase diagram."""
    # Triple point
    T_tp = 273.16
    P_tp = 611.7

    # Critical point
    T_c = 647.3
    P_c = 22.1e6

    # Solid-liquid line (slightly negative slope for water)
    T_sl = np.linspace(250, T_tp, 50)
    P_sl = P_tp * np.exp(-7.5e6 * 18e-6 / R * (1/T_sl - 1/T_tp))

    # Liquid-vapor line
    T_lv = np.linspace(T_tp, T_c, 100)
    L_vap = 2.26e6
    P_lv = P_tp * np.exp(-L_vap * 0.018 / R * (1/T_lv - 1/T_tp))

    # Solid-vapor line
    T_sv = np.linspace(200, T_tp, 50)
    L_sub = 2.83e6  # Sublimation
    P_sv = P_tp * np.exp(-L_sub * 0.018 / R * (1/T_sv - 1/T_tp))

    plt.figure(figsize=(10, 8))
    plt.semilogy(T_sl, P_sl, 'b-', linewidth=2, label='Solid-Liquid')
    plt.semilogy(T_lv, P_lv, 'r-', linewidth=2, label='Liquid-Vapor')
    plt.semilogy(T_sv, P_sv, 'g-', linewidth=2, label='Solid-Vapor')
    plt.plot(T_tp, P_tp, 'ko', markersize=10, label='Triple Point')
    plt.plot(T_c, P_c, 'r*', markersize=15, label='Critical Point')

    plt.xlabel('Temperature (K)')
    plt.ylabel('Pressure (Pa)')
    plt.title('Water Phase Diagram')
    plt.legend()
    plt.grid(True)
    plt.xlim(200, 700)
    plt.ylim(100, 1e8)
    plt.savefig('phase_diagram.png')
    plt.show()
```

## Atmospheric Thermodynamics

### Adiabatic Lapse Rate

```python
g = 9.81  # m/s²

def dry_adiabatic_lapse_rate(Cp=1005):
    """
    Dry adiabatic lapse rate: Γ = g/Cp

    Parameters:
        Cp: specific heat at constant pressure (J/kg/K)

    Returns:
        Gamma: lapse rate (K/m)
    """
    return g / Cp

Gamma = dry_adiabatic_lapse_rate()
print(f"Dry adiabatic lapse rate: {Gamma*1000:.1f} K/km")
# Output: Dry adiabatic lapse rate: 9.8 K/km
```

### Barometric Formula

```python
def pressure_altitude(z, T0=288, P0=101325, M=0.029):
    """
    Pressure vs altitude (isothermal approximation).

    P = P0 * exp(-Mgz/RT)
    """
    scale_height = R * T0 / (M * g)
    return P0 * np.exp(-z / scale_height)

def pressure_altitude_adiabatic(z, T0=288, P0=101325, gamma=1.4):
    """Pressure vs altitude (adiabatic atmosphere)."""
    Gamma = dry_adiabatic_lapse_rate()
    T = T0 - Gamma * z
    return P0 * (T / T0)**(g / (R * Gamma / 0.029))

# Compare at 5 km
z = 5000
P_iso = pressure_altitude(z)
P_adi = pressure_altitude_adiabatic(z)
print(f"At {z/1000} km:")
print(f"  Isothermal: {P_iso/1000:.1f} kPa")
print(f"  Adiabatic: {P_adi/1000:.1f} kPa")
```

### Potential Temperature

```python
def potential_temperature(T, P, P0=100000):
    """
    Potential temperature θ.

    θ = T * (P0/P)^(R/Cp) = T * (P0/P)^0.286
    """
    kappa = 0.286  # R/Cp for air
    return T * (P0 / P)**kappa

# Example
T = 250  # K at altitude
P = 50000  # Pa
theta = potential_temperature(T, P)
print(f"Potential temperature: {theta:.1f} K")
```

## Full Source Code

```
thermodynamics_solutions/python/chapter3_functions.py
```

## Related Resources

- [Chapter 3 Theory](/docs/problems/thermodynamics/functions)
- [LaTeX Solutions](/docs/solutions/latex/chapter3/problems-1073-1085)
- [Key Formulas](/docs/solutions/formulas)

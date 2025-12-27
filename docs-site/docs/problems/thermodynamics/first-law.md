---
sidebar_position: 1
---

# Chapter 1: Thermodynamic States and the First Law

## Overview

This chapter covers the foundational concepts of thermodynamics, including temperature, heat, work, and the first law. Problems 1001-1030 test understanding of:

- Temperature measurement and scales
- Heat capacity at constant pressure and volume
- Ideal gas processes (isothermal, isobaric, isochoric)
- Adiabatic processes
- Radiation and heat transfer

## Key Concepts

### The First Law of Thermodynamics

The first law is a statement of energy conservation:

$$
dU = \delta Q - \delta W
$$

Where:
- $dU$ = change in internal energy
- $\delta Q$ = heat added to the system
- $\delta W$ = work done by the system

### Ideal Gas Law

$$
PV = nRT
$$

Where:
- $P$ = pressure
- $V$ = volume
- $n$ = number of moles
- $R$ = gas constant (8.314 J/mol·K)
- $T$ = temperature

### Heat Capacities

For an ideal gas:
- **Constant volume**: $C_V = \frac{f}{2}R$ where $f$ is degrees of freedom
- **Constant pressure**: $C_P = C_V + R$
- **Ratio**: $\gamma = \frac{C_P}{C_V}$

| Gas Type | $f$ | $C_V$ | $C_P$ | $\gamma$ |
|----------|-----|-------|-------|----------|
| Monatomic | 3 | $\frac{3}{2}R$ | $\frac{5}{2}R$ | 5/3 |
| Diatomic | 5 | $\frac{5}{2}R$ | $\frac{7}{2}R$ | 7/5 |
| Polyatomic | 6 | $3R$ | $4R$ | 4/3 |

### Adiabatic Processes

For an adiabatic process ($\delta Q = 0$):

$$
PV^\gamma = \text{constant}
$$

$$
TV^{\gamma-1} = \text{constant}
$$

$$
TP^{(1-\gamma)/\gamma} = \text{constant}
$$

### Work Done

| Process | Work $W$ |
|---------|----------|
| Isobaric | $P\Delta V$ |
| Isochoric | $0$ |
| Isothermal | $nRT \ln(V_f/V_i)$ |
| Adiabatic | $\frac{P_iV_i - P_fV_f}{\gamma-1}$ |

## Problem Categories

### Temperature and Measurement (1001-1005)
- Thermometer calibration
- Temperature scales conversion
- Thermal equilibrium

### Heat Capacity (1006-1012)
- Specific heat calculations
- Dulong-Petit law
- Heat capacity ratios

### Ideal Gas Processes (1013-1020)
- PV diagrams
- Cyclic processes
- Work and heat calculations

### Adiabatic Processes (1021-1025)
- Adiabatic expansion/compression
- Sound propagation
- Atmospheric thermodynamics

### Radiation (1026-1030)
- Stefan-Boltzmann law: $P = \sigma A T^4$
- Wien's displacement law: $\lambda_{max} T = b$
- Blackbody radiation

## Related Resources

- [Problem Set 1001-1030](./first-law-problems)
- [Solutions: Chapter 1](/docs/solutions/latex/chapter1/problems-1001-1010)
- [Python Code: Chapter 1](/docs/code/python/chapter1-first-law)

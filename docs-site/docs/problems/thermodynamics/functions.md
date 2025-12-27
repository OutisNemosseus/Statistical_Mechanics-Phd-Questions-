---
sidebar_position: 5
---

# Chapter 3: Thermodynamic Functions and Potentials

## Overview

This chapter covers thermodynamic potentials and their applications. Problems 1073-1105 address:

- Helmholtz and Gibbs free energy
- Maxwell relations
- Clausius-Clapeyron equation
- Atmospheric thermodynamics
- Chemical potential

## Key Concepts

### Thermodynamic Potentials

| Potential | Definition | Natural Variables | Differential Form |
|-----------|------------|-------------------|-------------------|
| Internal Energy $U$ | Fundamental | $S, V$ | $dU = TdS - PdV$ |
| Enthalpy $H$ | $U + PV$ | $S, P$ | $dH = TdS + VdP$ |
| Helmholtz $F$ | $U - TS$ | $T, V$ | $dF = -SdT - PdV$ |
| Gibbs $G$ | $H - TS$ | $T, P$ | $dG = -SdT + VdP$ |

### Maxwell Relations

From the equality of mixed partial derivatives:

$$
\left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V
$$

$$
\left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P
$$

$$
\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V
$$

$$
\left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P
$$

### Clausius-Clapeyron Equation

For phase transitions:

$$
\frac{dP}{dT} = \frac{\Delta H}{T\Delta V} = \frac{L}{T\Delta V}
$$

For liquid-vapor equilibrium (ideal gas approximation):

$$
\frac{d\ln P}{dT} = \frac{L}{RT^2}
$$

Integrated form:
$$
\ln\frac{P_2}{P_1} = -\frac{L}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)
$$

### Chemical Potential

$$
\mu = \left(\frac{\partial G}{\partial n}\right)_{T,P} = \left(\frac{\partial F}{\partial n}\right)_{T,V}
$$

For an ideal gas:
$$
\mu = \mu^0(T) + RT\ln\frac{P}{P^0}
$$

### Response Functions

| Function | Definition | Relation |
|----------|------------|----------|
| Heat capacity $C_V$ | $\left(\frac{\partial U}{\partial T}\right)_V$ | $T\left(\frac{\partial S}{\partial T}\right)_V$ |
| Heat capacity $C_P$ | $\left(\frac{\partial H}{\partial T}\right)_P$ | $T\left(\frac{\partial S}{\partial T}\right)_P$ |
| Thermal expansion $\alpha$ | $\frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_P$ | |
| Isothermal compressibility $\kappa_T$ | $-\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T$ | |

### Important Relations

$$
C_P - C_V = \frac{TV\alpha^2}{\kappa_T}
$$

$$
\left(\frac{\partial U}{\partial V}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_V - P
$$

## Problem Categories

### Free Energy (1073-1080)
- Helmholtz free energy calculations
- Gibbs free energy and equilibrium
- Spontaneity criteria

### Maxwell Relations (1081-1090)
- Deriving thermodynamic identities
- Relating measurable quantities
- Proving thermodynamic relations

### Phase Transitions (1091-1100)
- Clausius-Clapeyron applications
- Triple point
- Critical phenomena

### Atmospheric Thermodynamics (1101-1105)
- Adiabatic lapse rate
- Atmospheric stability
- Moist air thermodynamics

## Related Resources

- [Problem Set 1073-1105](./functions-problems)
- [Solutions: Chapter 3](/docs/solutions/latex/chapter3/problems-1073-1085)
- [Python Code: Chapter 3](/docs/code/python/chapter3-functions)

---
sidebar_position: 3
---

# Chapter 2: The Second Law and Entropy

## Overview

This chapter covers the second law of thermodynamics and entropy. Problems 1031-1072 address:

- Carnot cycle and efficiency
- Heat engines and heat pumps
- Entropy calculations
- Irreversible processes
- Free expansion

## Key Concepts

### The Second Law of Thermodynamics

**Kelvin-Planck Statement:** No process is possible whose sole result is the complete conversion of heat into work.

**Clausius Statement:** No process is possible whose sole result is the transfer of heat from a cooler to a hotter body.

### Carnot Cycle

The most efficient heat engine operating between two temperatures:

$$
\eta_{Carnot} = 1 - \frac{T_C}{T_H}
$$

Where:
- $T_H$ = temperature of hot reservoir
- $T_C$ = temperature of cold reservoir

### Entropy

Entropy is defined as:

$$
dS = \frac{\delta Q_{rev}}{T}
$$

For any process:
$$
\Delta S_{universe} \geq 0
$$

### Entropy Changes

| Process | $\Delta S$ |
|---------|------------|
| Isothermal expansion | $nR \ln(V_f/V_i)$ |
| Heating at constant $V$ | $nC_V \ln(T_f/T_i)$ |
| Heating at constant $P$ | $nC_P \ln(T_f/T_i)$ |
| Free expansion | $nR \ln(V_f/V_i)$ |
| Mixing of ideal gases | $-R\sum n_i \ln x_i$ |
| Phase transition | $\frac{\Delta H}{T}$ |

### Heat Engines

**Efficiency:**
$$
\eta = \frac{W}{Q_H} = \frac{Q_H - Q_C}{Q_H} = 1 - \frac{Q_C}{Q_H}
$$

**Coefficient of Performance (Heat Pump):**
$$
COP_{HP} = \frac{Q_H}{W} = \frac{T_H}{T_H - T_C}
$$

**Coefficient of Performance (Refrigerator):**
$$
COP_{ref} = \frac{Q_C}{W} = \frac{T_C}{T_H - T_C}
$$

### Clausius Inequality

For any cyclic process:
$$
\oint \frac{\delta Q}{T} \leq 0
$$

Equality holds for reversible processes.

## Problem Categories

### Carnot Cycle (1031-1040)
- Efficiency calculations
- Reversible heat engines
- Combined cycles

### Heat Engines (1041-1050)
- Otto cycle
- Diesel cycle
- Stirling cycle
- Real engine efficiency

### Entropy Calculations (1051-1060)
- Entropy of ideal gases
- Entropy of mixing
- Phase transitions
- Irreversible processes

### Free Expansion (1061-1072)
- Joule expansion
- Joule-Thomson effect
- Entropy of the universe

## Important Formulas

### Entropy of Ideal Gas

$$
S = nC_V \ln T + nR \ln V + S_0
$$

or equivalently:

$$
S = nC_P \ln T - nR \ln P + S_0'
$$

### Gibbs Paradox

For mixing of identical gases:
$$
\Delta S_{mixing} = 0
$$

For mixing of different gases:
$$
\Delta S_{mixing} = -nR\sum_i x_i \ln x_i
$$

## Related Resources

- [Problem Set 1031-1072](./entropy-problems)
- [Solutions: Chapter 2](/docs/solutions/latex/chapter2/problems-1031-1040)
- [Python Code: Chapter 2](/docs/code/python/chapter2-entropy)

---
sidebar_position: 4
---

# Quantum Statistics

## Overview

At low temperatures or high densities, quantum effects become important. Particles obey either Fermi-Dirac (fermions) or Bose-Einstein (bosons) statistics.

## Fermi-Dirac Statistics

For fermions (spin-1/2 particles like electrons):

$$
\langle n_i \rangle = \frac{1}{e^{\beta(\varepsilon_i - \mu)} + 1}
$$

### Fermi Energy

At $T = 0$:
$$
\varepsilon_F = \frac{\hbar^2}{2m}\left(\frac{3\pi^2 N}{V}\right)^{2/3}
$$

### Low Temperature Behavior

At $T \ll T_F$:
$$
U \approx \frac{3}{5}N\varepsilon_F\left[1 + \frac{5\pi^2}{12}\left(\frac{T}{T_F}\right)^2\right]
$$

$$
C_V \approx \frac{\pi^2}{2}Nk_B\frac{T}{T_F}
$$

### Applications
- Electrons in metals
- White dwarf stars
- Neutron stars

## Bose-Einstein Statistics

For bosons (integer spin particles like photons):

$$
\langle n_i \rangle = \frac{1}{e^{\beta(\varepsilon_i - \mu)} - 1}
$$

### Bose-Einstein Condensation

Critical temperature:
$$
T_c = \frac{2\pi\hbar^2}{mk_B}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}
$$

Below $T_c$:
$$
\frac{N_0}{N} = 1 - \left(\frac{T}{T_c}\right)^{3/2}
$$

### Applications
- Liquid helium-4
- Ultracold atomic gases
- Photon gas

## Blackbody Radiation

### Planck Distribution
$$
u(\omega) = \frac{\hbar\omega^3}{\pi^2 c^3}\frac{1}{e^{\beta\hbar\omega} - 1}
$$

### Stefan-Boltzmann Law
$$
U = \frac{\pi^2 k_B^4}{15\hbar^3 c^3}VT^4 = aVT^4
$$

### Wien's Law
$$
\lambda_{max}T = 2.898 \times 10^{-3} \text{ m·K}
$$

## Comparison

| Property | Classical | Fermi-Dirac | Bose-Einstein |
|----------|-----------|-------------|---------------|
| Particles | Distinguishable | Identical fermions | Identical bosons |
| Occupation | Any | 0 or 1 | 0, 1, 2, ... |
| Statistics | Maxwell-Boltzmann | Fermi-Dirac | Bose-Einstein |
| Chemical potential | Any | $\mu \leq \varepsilon_{min}$ | $\mu \leq \varepsilon_{min}$ |

## Problem Types

1. Calculate Fermi energy for metals
2. Heat capacity of electron gas
3. Bose-Einstein condensation temperature
4. Blackbody radiation problems
5. Photon and phonon gases

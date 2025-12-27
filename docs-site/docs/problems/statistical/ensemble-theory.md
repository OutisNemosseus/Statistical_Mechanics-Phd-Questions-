---
sidebar_position: 3
---

# Ensemble Theory

## Overview

Ensemble theory provides a systematic framework for statistical mechanics, allowing calculation of macroscopic properties from microscopic states.

## Types of Ensembles

### Microcanonical Ensemble (NVE)

**Fixed quantities:** $N$, $V$, $E$

**Fundamental relation:**
$$
S = k_B \ln \Omega(N, V, E)
$$

**Use when:** System is isolated (no heat or particle exchange)

### Canonical Ensemble (NVT)

**Fixed quantities:** $N$, $V$, $T$

**Partition function:**
$$
Z = \sum_i e^{-\beta E_i} = \int \frac{d^{3N}p \, d^{3N}q}{h^{3N}N!} e^{-\beta H(p,q)}
$$

**Thermodynamic connection:**
$$
F = -k_BT \ln Z
$$

**Use when:** System in thermal contact with heat bath

### Grand Canonical Ensemble ($\mu$VT)

**Fixed quantities:** $\mu$, $V$, $T$

**Grand partition function:**
$$
\mathcal{Z} = \sum_{N=0}^{\infty} z^N Z_N = \sum_{N=0}^{\infty} e^{\beta\mu N} Z_N
$$

where $z = e^{\beta\mu}$ is the fugacity.

**Thermodynamic connection:**
$$
PV = k_BT \ln \mathcal{Z}
$$

**Use when:** System can exchange particles (open system)

## Partition Functions

### Ideal Gas (Canonical)

$$
Z = \frac{1}{N!}\left(\frac{V}{\lambda^3}\right)^N
$$

where $\lambda = \sqrt{\frac{h^2}{2\pi m k_BT}}$ is the thermal de Broglie wavelength.

### Harmonic Oscillator

**Classical:**
$$
Z_1 = \frac{k_BT}{\hbar\omega}
$$

**Quantum:**
$$
Z_1 = \frac{e^{-\beta\hbar\omega/2}}{1 - e^{-\beta\hbar\omega}} = \frac{1}{2\sinh(\beta\hbar\omega/2)}
$$

### Two-Level System

$$
Z_1 = 1 + e^{-\beta\varepsilon}
$$

## Fluctuations

### Energy Fluctuations (Canonical)
$$
\langle (\Delta E)^2 \rangle = k_BT^2 C_V
$$

### Particle Number Fluctuations (Grand Canonical)
$$
\langle (\Delta N)^2 \rangle = k_BT \left(\frac{\partial N}{\partial \mu}\right)_{T,V}
$$

## Problem Types

1. Calculate partition functions for various systems
2. Derive thermodynamic quantities from $Z$
3. Analyze fluctuations and their physical meaning
4. Compare results from different ensembles
5. Apply to magnetic systems, polymers, etc.

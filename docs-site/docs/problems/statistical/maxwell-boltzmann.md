---
sidebar_position: 2
---

# Maxwell-Boltzmann Statistics

## Overview

The Maxwell-Boltzmann distribution describes the statistical behavior of classical particles in thermal equilibrium.

## Key Distributions

### Velocity Distribution

The probability that a molecule has velocity components in the range $(v_x, v_x+dv_x)$, $(v_y, v_y+dv_y)$, $(v_z, v_z+dv_z)$:

$$
f(v_x, v_y, v_z) = \left(\frac{m}{2\pi k_BT}\right)^{3/2} \exp\left(-\frac{m(v_x^2+v_y^2+v_z^2)}{2k_BT}\right)
$$

### Speed Distribution

The probability that a molecule has speed in the range $(v, v+dv)$:

$$
f(v) = 4\pi n \left(\frac{m}{2\pi k_BT}\right)^{3/2} v^2 \exp\left(-\frac{mv^2}{2k_BT}\right)
$$

### Characteristic Speeds

| Speed | Expression | Value for air at 300K |
|-------|------------|----------------------|
| Most probable | $v_p = \sqrt{\frac{2k_BT}{m}}$ | 422 m/s |
| Mean | $\langle v \rangle = \sqrt{\frac{8k_BT}{\pi m}}$ | 476 m/s |
| RMS | $v_{rms} = \sqrt{\frac{3k_BT}{m}}$ | 517 m/s |

### Energy Distribution

$$
g(\varepsilon) = \frac{2\pi n}{(\pi k_BT)^{3/2}} \sqrt{\varepsilon} \exp\left(-\frac{\varepsilon}{k_BT}\right)
$$

## Equipartition Theorem

Each quadratic term in the Hamiltonian contributes $\frac{1}{2}k_BT$ to the average energy.

**Examples:**
- Translational motion (3D): $U = \frac{3}{2}k_BT$
- Diatomic molecule (rotation): $U = k_BT$
- Harmonic oscillator: $U = k_BT$

## Applications

### Effusion
Rate of molecules escaping through a small hole:
$$
\Phi = \frac{1}{4}n\langle v \rangle = \frac{P}{\sqrt{2\pi mk_BT}}
$$

### Mean Free Path
$$
\lambda = \frac{1}{\sqrt{2}n\sigma}
$$

where $\sigma = \pi d^2$ is the collision cross-section.

### Collision Rate
$$
Z = \sqrt{2}n\sigma\langle v \rangle
$$

## Problem Types

1. Calculate characteristic speeds for various gases
2. Find the fraction of molecules with speed > $v_0$
3. Derive transport coefficients (viscosity, thermal conductivity)
4. Analyze molecular beam experiments
5. Calculate pressure using kinetic theory

## Resources

- [PDF Resources](../pdf-index) - Original problems
- [Statistical Physics Overview](./intro)

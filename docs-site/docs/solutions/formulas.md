---
sidebar_position: 10
---

# Key Formulas

A quick reference for the most important thermodynamics and statistical mechanics formulas.

## Thermodynamics

### First Law

$$
dU = \delta Q - \delta W
$$

$$
dU = \delta Q - PdV \quad \text{(reversible work)}
$$

### Ideal Gas

$$
PV = nRT = Nk_BT
$$

$$
U = nC_VT = \frac{f}{2}nRT
$$

### Heat Capacities

$$
C_P - C_V = nR
$$

$$
\gamma = \frac{C_P}{C_V}
$$

| Gas Type | $C_V$ | $C_P$ | $\gamma$ |
|----------|-------|-------|----------|
| Monatomic | $\frac{3}{2}R$ | $\frac{5}{2}R$ | $\frac{5}{3}$ |
| Diatomic | $\frac{5}{2}R$ | $\frac{7}{2}R$ | $\frac{7}{5}$ |

### Adiabatic Processes

$$
PV^\gamma = \text{const}
$$

$$
TV^{\gamma-1} = \text{const}
$$

$$
TP^{(\gamma-1)/\gamma} = \text{const}
$$

### Work Done

| Process | $W$ |
|---------|-----|
| Isobaric | $P\Delta V$ |
| Isochoric | $0$ |
| Isothermal | $nRT\ln\frac{V_f}{V_i}$ |
| Adiabatic | $\frac{P_iV_i - P_fV_f}{\gamma-1} = \frac{nR(T_i-T_f)}{\gamma-1}$ |

---

## Second Law & Entropy

### Entropy

$$
dS = \frac{\delta Q_{rev}}{T}
$$

$$
\Delta S_{universe} \geq 0
$$

### Carnot Efficiency

$$
\eta = 1 - \frac{T_C}{T_H}
$$

### Entropy Changes

| Process | $\Delta S$ |
|---------|------------|
| Isothermal (ideal gas) | $nR\ln\frac{V_f}{V_i}$ |
| Heating at const $V$ | $nC_V\ln\frac{T_f}{T_i}$ |
| Heating at const $P$ | $nC_P\ln\frac{T_f}{T_i}$ |
| Phase transition | $\frac{L}{T}$ |
| Mixing (ideal gases) | $-R\sum n_i\ln x_i$ |

---

## Thermodynamic Potentials

### Definitions

| Potential | Definition | Differential |
|-----------|------------|--------------|
| $U$ | Internal energy | $TdS - PdV$ |
| $H = U + PV$ | Enthalpy | $TdS + VdP$ |
| $F = U - TS$ | Helmholtz | $-SdT - PdV$ |
| $G = H - TS$ | Gibbs | $-SdT + VdP$ |

### Maxwell Relations

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

### Clausius-Clapeyron

$$
\frac{dP}{dT} = \frac{L}{T\Delta V}
$$

---

## Statistical Mechanics

### Boltzmann Distribution

$$
P_i = \frac{e^{-\beta E_i}}{Z}, \quad \beta = \frac{1}{k_BT}
$$

### Partition Function

$$
Z = \sum_i e^{-\beta E_i}
$$

$$
F = -k_BT\ln Z
$$

$$
U = -\frac{\partial \ln Z}{\partial \beta}
$$

$$
S = k_B\left(\ln Z + \beta U\right)
$$

### Maxwell-Boltzmann Speed Distribution

$$
f(v) = 4\pi n\left(\frac{m}{2\pi k_BT}\right)^{3/2} v^2 e^{-mv^2/2k_BT}
$$

| Speed | Expression |
|-------|------------|
| Most probable | $v_p = \sqrt{2k_BT/m}$ |
| Mean | $\langle v\rangle = \sqrt{8k_BT/\pi m}$ |
| RMS | $v_{rms} = \sqrt{3k_BT/m}$ |

### Quantum Statistics

**Fermi-Dirac:**
$$
\langle n \rangle = \frac{1}{e^{\beta(\varepsilon-\mu)} + 1}
$$

**Bose-Einstein:**
$$
\langle n \rangle = \frac{1}{e^{\beta(\varepsilon-\mu)} - 1}
$$

### Blackbody Radiation

$$
u(\nu) = \frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT}-1}
$$

$$
P = \sigma T^4, \quad \sigma = 5.67 \times 10^{-8} \text{ W/(m²·K⁴)}
$$

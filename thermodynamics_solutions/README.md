# Thermodynamics & Statistical Mechanics - Solutions Package

## Overview

This package contains LaTeX solutions and Python/MATLAB code for problems from "Problems and Solutions on Thermodynamics & Statistical Mechanics" (SM10-110).

## Directory Structure

```
thermodynamics_solutions/
├── latex/
│   ├── main.tex                    # Master LaTeX document
│   ├── chapter1_first_law/         # Problems 1001-1030
│   │   ├── problems_1001_1010.tex
│   │   ├── problems_1011_1020.tex
│   │   └── problems_1021_1030.tex
│   ├── chapter2_entropy/           # Problems 1031-1072
│   │   ├── problems_1031_1040.tex
│   │   ├── problems_1041_1050.tex
│   │   ├── problems_1051_1060.tex
│   │   └── problems_1061_1072.tex
│   └── chapter3_functions/         # Problems 1073-1105
│       ├── problems_1073_1085.tex
│       ├── problems_1086_1100.tex
│       └── problems_1101_1105.tex
├── python/
│   ├── chapter1_first_law.py       # Computational solutions Ch.1
│   ├── chapter2_entropy.py         # Computational solutions Ch.2
│   └── chapter3_functions.py       # Computational solutions Ch.3
├── matlab/
│   └── chapter1_and_2.m            # MATLAB solutions
└── README.md                       # This file
```

## Topics Covered

### Part I: Thermodynamics

1. **Thermodynamic States and the First Law (Problems 1001-1030)**
   - Temperature measurement
   - Heat capacity
   - Ideal gas processes
   - Adiabatic processes
   - Radiation and heat transfer

2. **The Second Law and Entropy (Problems 1031-1072)**
   - Carnot cycle and efficiency
   - Heat engines and heat pumps
   - Entropy calculations
   - Irreversible processes
   - Free expansion

3. **Thermodynamic Functions (Problems 1073-1105)**
   - Helmholtz and Gibbs free energy
   - Maxwell relations
   - Clausius-Clapeyron equation
   - Atmospheric thermodynamics

## Compiling the LaTeX Document

```bash
cd latex
pdflatex main.tex
pdflatex main.tex  # Run twice for table of contents
```

## Running Python Code

```bash
cd python
python chapter1_first_law.py
python chapter2_entropy.py
python chapter3_functions.py
```

Required packages:
- numpy
- matplotlib
- scipy

## Running MATLAB Code

Open MATLAB and navigate to the `matlab/` directory, then run:
```matlab
chapter1_and_2
```

## Key Formulas Summary

### First Law
- dU = δQ - δW
- For ideal gas: pV = nRT
- Adiabatic process: pV^γ = const

### Second Law
- Carnot efficiency: η = 1 - T_cold/T_hot
- Entropy: dS = δQ_rev/T
- Free expansion: ΔS = nR ln(V_f/V_i)

### Thermodynamic Potentials
- Helmholtz: F = U - TS
- Gibbs: G = H - TS
- Maxwell relations (4 equations)

## Physical Constants Used

| Constant | Value | Unit |
|----------|-------|------|
| R (gas constant) | 8.314 | J/(mol·K) |
| σ (Stefan-Boltzmann) | 5.67×10⁻⁸ | W/(m²·K⁴) |
| k_B (Boltzmann) | 1.38×10⁻²³ | J/K |
| μ₀ (permeability) | 4π×10⁻⁷ | H/m |

## License

Educational use only. Based on physics problems from various universities.

## Contact

For questions about the solutions, please refer to the original textbook or consult a physics instructor.

---
sidebar_position: 1
---

# Code Overview

This section contains Python computational solutions for numerical problems in thermodynamics and statistical mechanics.

## Available Code

| Chapter | File | Topics |
|---------|------|--------|
| [Chapter 1](/docs/code/python/chapter1-first-law) | `chapter1_first_law.py` | Temperature, heat capacity, processes |
| [Chapter 2](/docs/code/python/chapter2-entropy) | `chapter2_entropy.py` | Carnot cycle, engines, entropy |
| [Chapter 3](/docs/code/python/chapter3-functions) | `chapter3_functions.py` | Maxwell relations, phase transitions |

## Repository Structure

```
thermodynamics_solutions/
├── python/
│   ├── chapter1_first_law.py    # First Law problems
│   ├── chapter2_entropy.py      # Entropy problems
│   └── chapter3_functions.py    # Thermodynamic functions
```

## Features

The Python code provides:

- **Numerical calculations** for complex problems
- **Visualization** of thermodynamic processes
- **Parameter studies** for exploring physics
- **Validation** of analytical solutions

## Dependencies

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import quad
```

### Installation

```bash
pip install numpy matplotlib scipy
```

## Physical Constants

All scripts use consistent constants:

```python
R = 8.314      # J/(mol·K) - Gas constant
k_B = 1.38e-23 # J/K - Boltzmann constant
sigma = 5.67e-8 # W/(m²·K⁴) - Stefan-Boltzmann
```

## Running the Code

```bash
cd thermodynamics_solutions/python

# Run individual chapter
python chapter1_first_law.py
python chapter2_entropy.py
python chapter3_functions.py
```

## Example Output

```
============================================================
Problem 1003: Bimetallic Strip
============================================================
Strip thickness: 2.0 mm
Temperature rise: 50 K
Radius of curvature: 3.3333 m = 333.33 cm

============================================================
Problem 1006: Heat Capacity of Copper Penny
============================================================
Mass of penny: 32 g
Heat capacity: 12.5 J/K = 3.0 cal/K
```

## Related Resources

- [Setup Guide](./setup)
- [LaTeX Solutions](/docs/solutions/intro)
- [Problems Overview](/docs/problems/intro)

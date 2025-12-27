---
sidebar_position: 10
---

# Setup Guide

Instructions for setting up and running the Python computational solutions.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/OutisNemosseus/Statistical_Mechanics-Phd-Questions-.git
cd Statistical_Mechanics-Phd-Questions-
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install numpy matplotlib scipy
```

Or create a `requirements.txt`:

```txt
numpy>=1.20.0
matplotlib>=3.4.0
scipy>=1.7.0
```

Then install:

```bash
pip install -r requirements.txt
```

## Directory Structure

```
Statistical_Mechanics-Phd-Questions-/
├── thermodynamics_solutions/
│   ├── latex/              # LaTeX solutions
│   ├── python/             # Python code
│   │   ├── chapter1_first_law.py
│   │   ├── chapter2_entropy.py
│   │   └── chapter3_functions.py
│   └── README.md
├── docs-site/              # Docusaurus website
└── *.pdf                   # Problem PDFs
```

## Running the Code

### Run All Problems in a Chapter

```bash
cd thermodynamics_solutions/python
python chapter1_first_law.py
```

### Run Specific Problems

The code is organized into functions. Import and call specific problems:

```python
from chapter1_first_law import problem_1003, problem_1006

# Problem 1003: Bimetallic strip
R = problem_1003(x=0.002, alpha1=12e-6, alpha2=24e-6, delta_T=50)
print(f"Radius of curvature: {R} m")

# Problem 1006: Heat capacity
Cv = problem_1006(mass_g=32, atomic_mass=64)
print(f"Heat capacity: {Cv} J/K")
```

### Generate Plots

Many problems include visualization:

```python
from chapter2_entropy import plot_carnot_cycle

# Generate PV diagram for Carnot cycle
plot_carnot_cycle(T_H=500, T_C=300, V1=1, V2=2)
plt.show()
```

## Troubleshooting

### Import Errors

If you get `ModuleNotFoundError`:

```bash
pip install numpy matplotlib scipy
```

### Path Issues

Make sure you're in the correct directory:

```bash
cd thermodynamics_solutions/python
```

### Permission Issues (Windows)

Run PowerShell as Administrator or use:

```bash
python -m pip install numpy matplotlib scipy
```

## IDE Recommendations

### VS Code

Install the Python extension and select your virtual environment.

### Jupyter Notebook

Convert scripts to notebooks for interactive exploration:

```bash
pip install jupyter
jupyter notebook
```

Then copy code into cells.

## Contributing

To add new solutions:

1. Follow the existing function naming convention: `problem_XXXX()`
2. Include docstrings with parameters and return values
3. Add example calculations with print statements
4. Test thoroughly before committing

## Related Resources

- [Code Overview](./intro)
- [Chapter 1 Code](./python/chapter1-first-law)
- [Chapter 2 Code](./python/chapter2-entropy)
- [Chapter 3 Code](./python/chapter3-functions)

"""
Thermodynamics Problems - Chapter 1: Thermodynamic States and the First Law
Problems 1001-1030 - Python Computational Solutions
"""

import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Physical Constants
R = 8.314  # J/(mol·K) - Universal gas constant
R_cal = 1.987  # cal/(mol·K)
sigma = 5.67e-8  # W/(m^2·K^4) - Stefan-Boltzmann constant
k_B = 1.38e-23  # J/K - Boltzmann constant
mu_0 = 4 * np.pi * 1e-7  # H/m - Permeability of free space

#=============================================================================
# Problem 1003: Bimetallic Strip Curvature
#=============================================================================
def problem_1003(x, alpha1, alpha2, delta_T):
    """
    Calculate the radius of curvature of a bimetallic strip.
    
    Parameters:
        x: total thickness of the strip (m)
        alpha1: coefficient of linear expansion of metal 1 (1/K)
        alpha2: coefficient of linear expansion of metal 2 (1/K), alpha2 > alpha1
        delta_T: temperature change (K)
    
    Returns:
        R: radius of curvature (m)
    """
    R = x / ((alpha2 - alpha1) * delta_T)
    return R

# Example calculation
print("=" * 60)
print("Problem 1003: Bimetallic Strip")
print("=" * 60)
x = 0.002  # 2 mm thickness
alpha1 = 12e-6  # steel
alpha2 = 24e-6  # brass
delta_T = 50  # 50 K temperature rise
R = problem_1003(x, alpha1, alpha2, delta_T)
print(f"Strip thickness: {x*1000:.1f} mm")
print(f"Temperature rise: {delta_T} K")
print(f"Radius of curvature: {R:.4f} m = {R*100:.2f} cm")
print()

#=============================================================================
# Problem 1006: Heat Capacity of Copper Penny
#=============================================================================
def problem_1006(mass_g, atomic_mass):
    """
    Calculate heat capacity of a copper penny using Dulong-Petit law.
    
    Parameters:
        mass_g: mass in grams
        atomic_mass: atomic mass (g/mol)
    
    Returns:
        Cv: heat capacity (J/K)
    """
    n_moles = mass_g / atomic_mass
    Cv = n_moles * 3 * R  # Dulong-Petit law: Cv = 3R per mole
    return Cv

print("=" * 60)
print("Problem 1006: Heat Capacity of Copper Penny")
print("=" * 60)
mass = 32  # grams
atomic_mass_Cu = 64  # g/mol
Cv = problem_1006(mass, atomic_mass_Cu)
print(f"Mass of penny: {mass} g")
print(f"Heat capacity: {Cv:.1f} J/K = {Cv/4.184:.1f} cal/K")
print()

#=============================================================================
# Problem 1008: Clement-Desormes Method for γ = Cp/Cv
#=============================================================================
def problem_1008(h_i, h_f):
    """
    Calculate γ = Cp/Cv using Clement-Desormes method.
    
    Parameters:
        h_i: initial manometer reading
        h_f: final manometer reading
    
    Returns:
        gamma: ratio of specific heats
    """
    gamma = h_i / (h_i - h_f)
    return gamma

print("=" * 60)
print("Problem 1008: Clement-Desormes Method")
print("=" * 60)
# Example: oxygen at 20°C
# Theoretical γ for diatomic gas = 7/5 = 1.4
h_i = 10  # arbitrary units
h_f = h_i * (1 - 1/1.4)  # back-calculated for γ = 1.4
gamma = problem_1008(h_i, h_f)
print(f"Initial reading h_i: {h_i}")
print(f"Final reading h_f: {h_f:.2f}")
print(f"Calculated γ: {gamma:.2f}")
print(f"Theoretical γ for O2 at 20°C: 1.4")
print()

#=============================================================================
# Problem 1012: Isothermal and Isobaric Expansion
#=============================================================================
def problem_1012(T0, V0_factor=2):
    """
    Calculate work and heat for isothermal and isobaric expansion.
    
    Parameters:
        T0: initial temperature (K)
        V0_factor: ratio V_final/V_initial
    
    Returns:
        dict with results for both processes
    """
    results = {}
    
    # (a) Isothermal expansion
    W_isothermal = R * T0 * np.log(V0_factor)
    Q_isothermal = W_isothermal  # ΔU = 0
    
    results['isothermal'] = {
        'W': W_isothermal,
        'Q': Q_isothermal,
        'ΔU': 0
    }
    
    # (b) Isobaric expansion (monatomic gas, Cv = 3R/2)
    # For isobaric: T_final/T_initial = V_final/V_initial
    T_final = T0 * V0_factor
    delta_T = T_final - T0
    W_isobaric = R * delta_T  # W = p*ΔV = nRΔT
    delta_U = 1.5 * R * delta_T  # Cv = 3R/2 for monatomic
    Q_isobaric = delta_U + W_isobaric
    
    results['isobaric'] = {
        'W': W_isobaric,
        'Q': Q_isobaric,
        'ΔU': delta_U
    }
    
    return results

print("=" * 60)
print("Problem 1012: Expansion of Monatomic Ideal Gas")
print("=" * 60)
T0 = 300  # K
results = problem_1012(T0)
print(f"Initial temperature: {T0} K")
print(f"Volume expansion: V0 → 2V0")
print()
print("Isothermal expansion (constant T):")
print(f"  Work done: W = RT₀ ln(2) = {results['isothermal']['W']:.1f} J")
print(f"  Heat absorbed: Q = {results['isothermal']['Q']:.1f} J")
print()
print("Isobaric expansion (constant p):")
print(f"  Work done: W = RT₀ = {results['isobaric']['W']:.1f} J")
print(f"  ΔU = (3/2)RT₀ = {results['isobaric']['ΔU']:.1f} J")
print(f"  Heat absorbed: Q = (5/2)RT₀ = {results['isobaric']['Q']:.1f} J")
print()

#=============================================================================
# Problem 1015: Adiabatic Compression Temperature
#=============================================================================
def problem_1015(T_initial, p_ratio, gamma):
    """
    Calculate final temperature after adiabatic compression.
    
    Parameters:
        T_initial: initial temperature (K)
        p_ratio: pressure ratio (p_final/p_initial)
        gamma: ratio of specific heats Cp/Cv
    
    Returns:
        T_final: final temperature (K)
    """
    T_final = T_initial * (p_ratio ** ((gamma - 1) / gamma))
    return T_final

print("=" * 60)
print("Problem 1015: Adiabatic Compression")
print("=" * 60)
T_initial = 300  # K
p_ratio = 10  # from 1 atm to 10 atm

# Air (diatomic)
gamma_air = 1.4
T_air = problem_1015(T_initial, p_ratio, gamma_air)
print(f"Initial: T = {T_initial} K, p = 1 atm → p = 10 atm")
print(f"Air (γ = {gamma_air}): T_final = {T_air:.1f} K")

# Helium (monatomic)
gamma_He = 5/3
T_He = problem_1015(T_initial, p_ratio, gamma_He)
print(f"Helium (γ = {gamma_He:.3f}): T_final = {T_He:.1f} K")
print()

#=============================================================================
# Problem 1016: Isothermal and Adiabatic Work
#=============================================================================
def problem_1016(T_i_celsius, V_ratio, gamma=5/3):
    """
    Calculate work for isothermal expansion and final temperature for adiabatic.
    
    Parameters:
        T_i_celsius: initial temperature in Celsius
        V_ratio: volume expansion ratio
        gamma: ratio of specific heats (default: monatomic gas)
    
    Returns:
        W: work done in isothermal process (J)
        T_f: final temperature in adiabatic process (K)
    """
    T_i = T_i_celsius + 273.15  # Convert to Kelvin
    
    # (a) Isothermal work
    W = R * T_i * np.log(V_ratio)
    
    # (b) Adiabatic final temperature
    # TV^(γ-1) = const
    T_f = T_i * (1/V_ratio) ** (gamma - 1)
    
    return W, T_f

print("=" * 60)
print("Problem 1016: Isothermal and Adiabatic Expansion")
print("=" * 60)
T_i = 0  # °C
V_ratio = 10

W, T_f = problem_1016(T_i, V_ratio)
print(f"Initial temperature: {T_i}°C = {T_i + 273.15} K")
print(f"Volume expansion: V₀ → 10V₀")
print()
print(f"(a) Isothermal work: W = RT ln(10) = {W:.1f} J = {W/1000:.2f} kJ")
print(f"(b) Adiabatic final T (monatomic): {T_f:.1f} K = {T_f - 273.15:.1f}°C")
print()

#=============================================================================
# Problem 1017: Heating Nitrogen
#=============================================================================
def problem_1017(mass_g, T1_C, T2_C, cv_cal=5, R_cal=2):
    """
    Calculate heat, work, and internal energy change for heating nitrogen.
    
    Parameters:
        mass_g: mass of nitrogen in grams
        T1_C: initial temperature in Celsius
        T2_C: final temperature in Celsius
        cv_cal: molar heat capacity at constant volume (cal/mol·K)
        R_cal: gas constant in cal/mol·K
    
    Returns:
        dict with Q_p, ΔU, W, Q_v
    """
    M_N2 = 28  # g/mol
    n = mass_g / M_N2  # moles
    delta_T = T2_C - T1_C
    
    cp_cal = cv_cal + R_cal
    
    # (a) Heat at constant pressure
    Q_p = n * cp_cal * delta_T
    
    # (b) Internal energy increase
    delta_U = n * cv_cal * delta_T
    
    # (c) External work
    W = Q_p - delta_U
    
    # (d) Heat at constant volume
    Q_v = delta_U
    
    return {
        'Q_p': Q_p,
        'ΔU': delta_U,
        'W': W,
        'Q_v': Q_v,
        'n': n
    }

print("=" * 60)
print("Problem 1017: Heating Nitrogen")
print("=" * 60)
results = problem_1017(1000, -20, 100)
print(f"Mass: 1000 g N₂, T: -20°C → 100°C")
print(f"Number of moles: {results['n']:.2f}")
print()
print(f"(a) Heat at constant pressure: Q = {results['Q_p']:.0f} cal = {results['Q_p']/1000:.1f} kcal")
print(f"(b) Internal energy increase: ΔU = {results['ΔU']:.0f} cal = {results['ΔU']/1000:.1f} kcal")
print(f"(c) External work: W = {results['W']:.0f} cal = {results['W']/1000:.1f} kcal")
print(f"(d) Heat at constant volume: Q_v = {results['Q_v']:.0f} cal = {results['Q_v']/1000:.1f} kcal")
print()

#=============================================================================
# Problem 1018: Isothermal Compression + Adiabatic Expansion
#=============================================================================
def problem_1018():
    """
    Analyze isothermal compression followed by adiabatic expansion.
    Creates pV diagram for monatomic and diatomic gases.
    """
    VA = 10  # liters
    VB = 1   # liters
    VC = 10  # liters
    pA = 1   # atm
    
    # Isothermal A→B: pV = const
    pB = pA * VA / VB  # = 10 atm
    
    # Adiabatic B→C: pV^γ = const
    gamma_mono = 5/3  # monatomic
    gamma_di = 7/5    # diatomic
    
    pC_mono = pB * (VB/VC)**gamma_mono
    pC_di = pB * (VB/VC)**gamma_di
    
    return {
        'pA': pA, 'VA': VA,
        'pB': pB, 'VB': VB,
        'pC_mono': pC_mono, 'pC_di': pC_di, 'VC': VC,
        'gamma_mono': gamma_mono, 'gamma_di': gamma_di
    }

print("=" * 60)
print("Problem 1018: Isothermal + Adiabatic Process")
print("=" * 60)
r = problem_1018()
print(f"Point A: p = {r['pA']} atm, V = {r['VA']} L")
print(f"Point B (after isothermal compression): p = {r['pB']} atm, V = {r['VB']} L")
print(f"Point C (after adiabatic expansion):")
print(f"  Monatomic (γ = {r['gamma_mono']:.3f}): pC = {r['pC_mono']:.3f} atm")
print(f"  Diatomic (γ = {r['gamma_di']:.3f}): pC = {r['pC_di']:.3f} atm")
print("Net work is done ON the system (compression curve above expansion)")
print()

#=============================================================================
# Problem 1019: Simple Harmonic Motion of Ball in Tube
#=============================================================================
def problem_1019(V0, A, M, p0, gamma):
    """
    Calculate oscillation frequency of ball in tube connected to gas jar.
    
    Parameters:
        V0: volume of jar (m³)
        A: cross-sectional area of tube (m²)
        M: mass of ball (kg)
        p0: atmospheric pressure (Pa)
        gamma: ratio of specific heats
    
    Returns:
        f: oscillation frequency (Hz)
    """
    g = 9.8  # m/s²
    p = p0 + M * g / A  # pressure in jar
    k = gamma * A**2 * p / V0  # effective spring constant
    omega = np.sqrt(k / M)
    f = omega / (2 * np.pi)
    return f

print("=" * 60)
print("Problem 1019: Ball Oscillation in Tube")
print("=" * 60)
V0 = 0.01  # 10 L = 0.01 m³
A = 0.001  # 10 cm² = 0.001 m²
M = 0.1    # 100 g = 0.1 kg
p0 = 101325  # Pa
gamma = 1.4  # air

f = problem_1019(V0, A, M, p0, gamma)
print(f"Jar volume: {V0*1000} L")
print(f"Tube area: {A*10000} cm²")
print(f"Ball mass: {M*1000} g")
print(f"Oscillation frequency: f = {f:.2f} Hz")
print()

#=============================================================================
# Problem 1020: Speed of Sound in Gas
#=============================================================================
def problem_1020(T, M, gamma=None, isothermal=False):
    """
    Calculate speed of sound in ideal gas.
    
    Parameters:
        T: temperature (K)
        M: molar mass (kg/mol)
        gamma: ratio of specific heats (for adiabatic)
        isothermal: if True, calculate isothermal sound speed
    
    Returns:
        c: speed of sound (m/s)
    """
    if isothermal:
        c = np.sqrt(R * T / M)
    else:
        c = np.sqrt(gamma * R * T / M)
    return c

print("=" * 60)
print("Problem 1020: Speed of Sound")
print("=" * 60)
T = 293  # K (20°C)
M_air = 0.029  # kg/mol

c_isothermal = problem_1020(T, M_air, isothermal=True)
c_adiabatic = problem_1020(T, M_air, gamma=1.4)

print(f"Temperature: {T} K")
print(f"Air (M = 29 g/mol)")
print(f"Isothermal sound speed: c = √(RT/M) = {c_isothermal:.1f} m/s")
print(f"Adiabatic sound speed: c = √(γRT/M) = {c_adiabatic:.1f} m/s")
print(f"Actual speed of sound in air ≈ 343 m/s (agrees with adiabatic)")
print()

#=============================================================================
# Problem 1022: Solenoid Coil Calculations
#=============================================================================
def problem_1022():
    """
    Calculate electrical and thermal properties of solenoid coil.
    """
    # Given data
    B = 0.25  # Tesla
    N = 100   # turns
    L = 4     # m (length)
    d = 3     # m (diameter)
    rho_Al = 3e-8  # Ω·m (resistivity of aluminum)
    A_conductor = (4*2 - 2*1) * 1e-4  # m² (cross-section minus cooling hole)
    c_water = 4190  # J/(kg·K)
    
    # (a) Current, resistance, voltage, power
    I = B * L / (mu_0 * N)
    L_wire = N * np.pi * d
    R = rho_Al * L_wire / A_conductor
    V = R * I
    P = V * I
    
    # (b) Water flow rate
    delta_T = 40  # K
    W = P / (1000 * c_water * delta_T)  # L/s
    
    # (c) Magnetic pressure
    p_mag = B**2 / (2 * mu_0)
    
    # (d) Time constant
    L_inductance = N * B * np.pi * (d/2)**2 / I
    tau = L_inductance / R
    t_99 = tau * np.log(100)
    
    return {
        'I': I, 'R': R, 'V': V, 'P': P/1000,  # P in kW
        'W': W, 'p_mag': p_mag,
        'L': L_inductance, 'tau': tau, 't_99': t_99
    }

print("=" * 60)
print("Problem 1022: Solenoid Coil")
print("=" * 60)
r = problem_1022()
print(f"(a) Current: I = {r['I']:.0f} A")
print(f"    Resistance: R = {r['R']*1000:.2f} mΩ")
print(f"    Voltage: V = {r['V']:.0f} V")
print(f"    Power: P = {r['P']:.1f} kW")
print(f"(b) Water flow rate: {r['W']:.1f} L/s")
print(f"(c) Magnetic pressure: {r['p_mag']:.2e} N/m²")
print(f"(d) Inductance: L = {r['L']*1000:.2f} mH")
print(f"    Time constant: τ = {r['tau']*1000:.1f} ms")
print(f"    Time to 99%: t = {r['t_99']*1000:.1f} ms")
print()

#=============================================================================
# Problem 1024: Radiation Heat Shield
#=============================================================================
def problem_1024(T1, T2, R_reflectivity):
    """
    Calculate heat shield properties in cryogenic system.
    
    Parameters:
        T1: cold temperature (K)
        T2: hot temperature (K)
        R_reflectivity: reflectivity of heat shield
    
    Returns:
        dict with T3 (shield temperature) and flux ratio
    """
    # Energy flux without shield
    J = sigma * (T2**4 - T1**4)
    
    # Shield temperature
    T3 = ((T1**4 + T2**4) / 2) ** 0.25
    
    # Energy flux with shield
    J_star = (1 - R_reflectivity) * J / 2
    
    return {
        'J': J, 'J_star': J_star,
        'T3': T3,
        'ratio': J_star / J
    }

print("=" * 60)
print("Problem 1024: Radiation Heat Shield (Dewar)")
print("=" * 60)
T1 = 4.2   # K (liquid He)
T2 = 300   # K (room temperature)
R = 0.95   # 95% reflectivity

r = problem_1024(T1, T2, R)
print(f"Cold side: {T1} K (liquid He)")
print(f"Hot side: {T2} K (room temperature)")
print(f"Shield reflectivity: {R*100}%")
print()
print(f"Shield temperature: T₃ = {r['T3']:.0f} K")
print(f"Flux without shield: J = {r['J']:.1f} W/m²")
print(f"Flux with shield: J* = {r['J_star']:.2f} W/m²")
print(f"Reduction ratio: J*/J = {r['ratio']:.3f} (reduced to {r['ratio']*100:.1f}%)")
print()

#=============================================================================
# Problem 1027: Solar Temperature
#=============================================================================
def problem_1027(J_earth=0.1e4, r_sun=7e8, r_SE=1.5e11):
    """
    Calculate sun's temperature from solar constant.
    
    Parameters:
        J_earth: solar constant at Earth (W/m²)
        r_sun: radius of sun (m)
        r_SE: sun-earth distance (m)
    
    Returns:
        T_sun: temperature of sun (K)
    """
    # J_earth = σT⁴(r_sun/r_SE)²
    T_sun = (J_earth * (r_SE/r_sun)**2 / sigma) ** 0.25
    return T_sun

print("=" * 60)
print("Problem 1027: Solar Temperature")
print("=" * 60)
T_sun = problem_1027()
print(f"Solar constant at Earth: 0.1 W/cm² = 1000 W/m²")
print(f"Sun radius: 7×10⁵ km")
print(f"Sun-Earth distance: 1.5×10⁸ km")
print(f"Calculated sun temperature: T = {T_sun:.0f} K")
print()

#=============================================================================
# Problem 1030: Neptune Surface Temperature
#=============================================================================
def problem_1030():
    """
    Estimate Neptune's surface temperature.
    """
    T_sun = 6000  # K
    r_sun = 7e8   # m
    r_SE = 1.5e11  # m (sun-earth distance)
    r_SN = 4.5e12  # m (sun-neptune distance)
    J_earth = 1400  # W/m² (solar constant at Earth)
    
    # Flux at Neptune
    J_neptune = J_earth * (r_SE / r_SN)**2
    
    # Equilibrium temperature (assuming black body)
    # J_neptune = 4σT⁴ (factor 4 from geometry)
    T_neptune = (J_neptune / (4 * sigma)) ** 0.25
    
    return T_neptune, J_neptune

print("=" * 60)
print("Problem 1030: Neptune Surface Temperature")
print("=" * 60)
T_N, J_N = problem_1030()
print(f"Sun-Neptune distance: 4.5×10⁹ km")
print(f"Solar flux at Neptune: {J_N:.3f} W/m²")
print(f"Estimated surface temperature: T = {T_N:.0f} K")
print()

#=============================================================================
# Main Execution
#=============================================================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("All calculations completed!")
    print("=" * 60)

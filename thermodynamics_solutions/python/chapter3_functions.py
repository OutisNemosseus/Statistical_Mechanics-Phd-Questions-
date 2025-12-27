"""
Thermodynamics Problems - Chapter 3: Thermodynamic Functions
Problems 1073-1105 - Python Computational Solutions
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical Constants
R = 8.314          # J/(mol·K)
g = 9.81           # m/s²
k_B = 1.38e-23     # J/K

#=============================================================================
# Problem 1097-1101: Atmospheric Thermodynamics
#=============================================================================

def isothermal_atmosphere(z, p0, T0, mu):
    """
    Calculate pressure in isothermal atmosphere.
    
    Parameters:
        z: height (m)
        p0: sea level pressure (Pa)
        T0: temperature (K)
        mu: molecular weight (kg/mol)
    
    Returns:
        p: pressure at height z (Pa)
    """
    H = R * T0 / (mu * g)  # scale height
    return p0 * np.exp(-z / H)

def adiabatic_atmosphere(z, p0, T0, mu, gamma):
    """
    Calculate pressure and temperature in adiabatic atmosphere.
    
    Parameters:
        z: height (m)
        p0: sea level pressure (Pa)
        T0: sea level temperature (K)
        mu: molecular weight (kg/mol)
        gamma: ratio of specific heats
    
    Returns:
        p: pressure at height z (Pa)
        T: temperature at height z (K)
    """
    # Temperature lapse rate
    dTdz = -(gamma - 1) / gamma * mu * g / R
    
    # Temperature at height z
    T = T0 + dTdz * z
    
    # Pressure at height z
    exponent = gamma / (gamma - 1)
    p = p0 * (T / T0) ** exponent
    
    return p, T, dTdz

def scale_height(T, mu):
    """Calculate atmospheric scale height."""
    return R * T / (mu * g)

print("=" * 60)
print("Problem 1097-1101: Atmospheric Thermodynamics")
print("=" * 60)

# Parameters for Earth's atmosphere
p0 = 101325  # Pa (sea level)
T0 = 288     # K (15°C)
mu_air = 0.029  # kg/mol
gamma_air = 1.4

# Scale height
H = scale_height(T0, mu_air)
print(f"\nEarth's Atmosphere Parameters:")
print(f"  Sea level pressure: p0 = {p0} Pa")
print(f"  Sea level temperature: T0 = {T0} K")
print(f"  Molecular weight: μ = {mu_air*1000:.0f} g/mol")
print(f"  Scale height: H = {H/1000:.1f} km")

# Adiabatic lapse rate
p_adi, T_adi, dTdz = adiabatic_atmosphere(1000, p0, T0, mu_air, gamma_air)
print(f"\nAdiabatic Lapse Rate:")
print(f"  dT/dz = {dTdz*1000:.2f} K/km")
print(f"  At 1 km: T = {T_adi:.1f} K, p = {p_adi:.0f} Pa")

# Isothermal atmosphere
p_iso = isothermal_atmosphere(1000, p0, T0, mu_air)
print(f"\nIsothermal Atmosphere at 1 km:")
print(f"  p = {p_iso:.0f} Pa")

# Plot pressure vs altitude
z = np.linspace(0, 20000, 100)  # 0 to 20 km

p_isothermal = isothermal_atmosphere(z, p0, T0, mu_air)
p_adiabatic, T_adiabatic, _ = adiabatic_atmosphere(z, p0, T0, mu_air, gamma_air)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(p_isothermal/1000, z/1000, 'b-', label='Isothermal', linewidth=2)
plt.plot(p_adiabatic/1000, z/1000, 'r-', label='Adiabatic', linewidth=2)
plt.xlabel('Pressure (kPa)')
plt.ylabel('Altitude (km)')
plt.title('Atmospheric Pressure vs Altitude')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim([0, 110])

plt.subplot(1, 2, 2)
plt.plot(T_adiabatic, z/1000, 'r-', linewidth=2)
plt.axhline(y=z[T_adiabatic > 0][-1]/1000, color='k', linestyle='--', alpha=0.5)
plt.xlabel('Temperature (K)')
plt.ylabel('Altitude (km)')
plt.title('Adiabatic Temperature vs Altitude')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('atmosphere_profiles.png', dpi=150)
plt.close()
print("\nSaved: atmosphere_profiles.png")
print()

#=============================================================================
# Maxwell Relations Verification
#=============================================================================
print("=" * 60)
print("Maxwell Relations")
print("=" * 60)

print("""
The four Maxwell relations derived from thermodynamic potentials:

1. From U(S,V): (∂T/∂V)_S = -(∂p/∂S)_V

2. From H(S,p): (∂T/∂p)_S = (∂V/∂S)_p

3. From F(T,V): (∂S/∂V)_T = (∂p/∂T)_V

4. From G(T,p): (∂S/∂p)_T = -(∂V/∂T)_p

For an ideal gas pV = nRT, we can verify relation 3:
  (∂S/∂V)_T = nR/V
  (∂p/∂T)_V = nR/V ✓
""")

#=============================================================================
# Clausius-Clapeyron Equation
#=============================================================================
print("=" * 60)
print("Clausius-Clapeyron Equation")
print("=" * 60)

def clausius_clapeyron(L, T, delta_V):
    """
    Calculate dp/dT using Clausius-Clapeyron equation.
    
    Parameters:
        L: latent heat (J/mol)
        T: temperature (K)
        delta_V: volume change (m³/mol)
    
    Returns:
        dpdT: pressure change rate (Pa/K)
    """
    return L / (T * delta_V)

# Example: Water boiling at 100°C
L_water = 40.7e3  # J/mol (latent heat of vaporization)
T_boil = 373.15   # K
V_gas = R * T_boil / 101325  # m³/mol (ideal gas)
V_liquid = 18e-6  # m³/mol
delta_V = V_gas - V_liquid

dpdT = clausius_clapeyron(L_water, T_boil, delta_V)

print(f"\nWater at boiling point (100°C):")
print(f"  Latent heat: L = {L_water/1000:.1f} kJ/mol")
print(f"  V_gas ≈ {V_gas*1000:.2f} L/mol")
print(f"  V_liquid ≈ {V_liquid*1e6:.0f} mL/mol")
print(f"  dp/dT = {dpdT:.0f} Pa/K = {dpdT/1000:.2f} kPa/K")
print()

#=============================================================================
# Joule-Thomson Effect
#=============================================================================
print("=" * 60)
print("Joule-Thomson Effect")
print("=" * 60)

def joule_thomson_ideal():
    """For ideal gas, Joule-Thomson coefficient is zero."""
    return 0

def joule_thomson_vdw(a, b, Cp, T, V):
    """
    Joule-Thomson coefficient for Van der Waals gas.
    
    Parameters:
        a, b: Van der Waals constants
        Cp: heat capacity at constant pressure
        T: temperature
        V: molar volume
    
    Returns:
        mu_JT: Joule-Thomson coefficient (K/Pa)
    """
    # μ_JT = (1/Cp)[T(∂V/∂T)_p - V]
    # For VdW gas: μ_JT ≈ (2a/RT - b) / Cp
    mu_JT = (2*a/(R*T) - b) / Cp
    return mu_JT

# Example: Nitrogen
a_N2 = 0.1408  # Pa·m⁶/mol²
b_N2 = 3.913e-5  # m³/mol
Cp_N2 = 29.1  # J/(mol·K)
T = 300  # K

mu_JT = joule_thomson_vdw(a_N2, b_N2, Cp_N2, T, None)
print(f"\nNitrogen at room temperature:")
print(f"  Van der Waals constants: a = {a_N2}, b = {b_N2}")
print(f"  Joule-Thomson coefficient: μ_JT ≈ {mu_JT*1e6:.3f} K/MPa")

# Inversion temperature
T_inv = 2*a_N2 / (R * b_N2)
print(f"  Inversion temperature: T_inv = {T_inv:.0f} K")
print()

#=============================================================================
# Gibbs-Helmholtz Equation
#=============================================================================
print("=" * 60)
print("Gibbs-Helmholtz Equation")
print("=" * 60)

print("""
The Gibbs-Helmholtz equation relates G, H, and T:

    ∂(G/T)/∂T|_p = -H/T²

Or equivalently:

    G = H + T(∂G/∂T)_p

This is useful for calculating reaction enthalpies from 
Gibbs free energy measurements at different temperatures.

For an ideal gas:
    G = G° + RT ln(p/p°)
    
    ∂(G/T)/∂T = -H°/T² + R ln(p/p°) · ∂(1)/∂T
              = -H/T²
""")

#=============================================================================
# Chemical Potential
#=============================================================================
print("=" * 60)
print("Chemical Potential")
print("=" * 60)

def chemical_potential_ideal_gas(mu0, T, p, p0=101325):
    """
    Chemical potential for ideal gas.
    
    Parameters:
        mu0: standard chemical potential
        T: temperature (K)
        p: pressure (Pa)
        p0: standard pressure (Pa)
    
    Returns:
        mu: chemical potential
    """
    return mu0 + R * T * np.log(p / p0)

print("""
Chemical potential μ is defined as:

    μ_i = (∂G/∂n_i)_{T,p,n_j≠i}

For an ideal gas mixture:
    μ_i = μ_i° + RT ln(p_i/p°)

At equilibrium, the chemical potential is uniform throughout:
    μ_i(phase 1) = μ_i(phase 2)
""")

#=============================================================================
# Adiabatic Demagnetization (Problem 1095)
#=============================================================================
print("=" * 60)
print("Problem 1095: Adiabatic Demagnetization")
print("=" * 60)

def adiabatic_demagnetization(Ti, Hi, Hf):
    """
    Calculate final temperature after adiabatic demagnetization.
    
    For a paramagnetic salt following Curie's law.
    
    Parameters:
        Ti: initial temperature (K)
        Hi: initial magnetic field (T)
        Hf: final magnetic field (T)
    
    Returns:
        Tf: final temperature (K)
    """
    return Ti * Hf / Hi

Ti = 1.0  # K
Hi = 5.0  # T
Hf = 0.01  # T

Tf = adiabatic_demagnetization(Ti, Hi, Hf)

print(f"\nAdiabatic demagnetization cooling:")
print(f"  Initial: Ti = {Ti} K, Hi = {Hi} T")
print(f"  Final: Hf = {Hf} T")
print(f"  Final temperature: Tf = Ti × (Hf/Hi) = {Tf*1000:.1f} mK")
print(f"  Cooling factor: {Ti/Tf:.0f}×")
print()

#=============================================================================
# Summary
#=============================================================================
print("=" * 60)
print("Summary of Key Results")
print("=" * 60)
print("""
1. Atmospheric scale height: H = RT/μg ≈ 8.4 km for Earth

2. Adiabatic lapse rate: dT/dz ≈ -9.8 K/km

3. Clausius-Clapeyron for water: dp/dT ≈ 3.6 kPa/K at 100°C

4. Joule-Thomson inversion temperature: T_inv = 2a/(Rb)

5. Adiabatic demagnetization: Tf/Ti = Hf/Hi
""")

if __name__ == "__main__":
    print("\nAll Chapter 3 calculations completed!")

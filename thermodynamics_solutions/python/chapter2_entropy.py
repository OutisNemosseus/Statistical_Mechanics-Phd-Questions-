"""
Thermodynamics Problems - Chapter 2: The Second Law and Entropy
Problems 1031-1072 - Python Computational Solutions
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical Constants
R = 8.314  # J/(mol·K) - Universal gas constant
R_cal = 1.987  # cal/(mol·K)
sigma = 5.67e-8  # W/(m^2·K^4) - Stefan-Boltzmann constant

#=============================================================================
# Problem 1031: Steam Turbine Maximum Work
#=============================================================================
def problem_1031(T_intake_C, T_exhaust_C, Q):
    """
    Calculate maximum work from steam turbine.
    
    Parameters:
        T_intake_C: intake temperature in Celsius
        T_exhaust_C: exhaust temperature in Celsius
        Q: heat input
    
    Returns:
        W_max: maximum work
        efficiency: Carnot efficiency
    """
    T1 = T_intake_C + 273.15  # K
    T2 = T_exhaust_C + 273.15  # K
    
    efficiency = 1 - T2/T1
    W_max = efficiency * Q
    
    return W_max, efficiency

print("=" * 60)
print("Problem 1031: Steam Turbine Maximum Work")
print("=" * 60)
Q = 1000  # arbitrary heat input
W_max, eta = problem_1031(400, 150, Q)
print(f"Intake temperature: 400°C = 673 K")
print(f"Exhaust temperature: 150°C = 423 K")
print(f"Carnot efficiency: η = {eta:.3f} = {eta*100:.1f}%")
print(f"Maximum work: W_max = {eta:.3f} × Q")
print()

#=============================================================================
# Problem 1032: Carnot Cycle Efficiency
#=============================================================================
def carnot_efficiency(T_hot, T_cold):
    """Calculate Carnot efficiency."""
    return 1 - T_cold / T_hot

def plot_carnot_cycle():
    """Plot Carnot cycle on pV and TS diagrams."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Parameters
    T1, T2 = 600, 300  # K (hot and cold)
    V_A, V_B = 1, 2
    gamma = 5/3
    
    # Calculate state points
    V_C = V_B * (T1/T2)**(1/(gamma-1))
    V_D = V_A * (T1/T2)**(1/(gamma-1))
    
    # pV diagram
    V_iso1 = np.linspace(V_A, V_B, 50)
    p_iso1 = T1 / V_iso1  # isothermal at T1
    
    V_adi1 = np.linspace(V_B, V_C, 50)
    p_adi1 = T1 * V_B**(gamma-1) / V_adi1**gamma
    
    V_iso2 = np.linspace(V_C, V_D, 50)
    p_iso2 = T2 / V_iso2  # isothermal at T2
    
    V_adi2 = np.linspace(V_D, V_A, 50)
    p_adi2 = T2 * V_D**(gamma-1) / V_adi2**gamma
    
    ax1.plot(V_iso1, p_iso1, 'r-', linewidth=2, label=f'Isothermal T={T1}K')
    ax1.plot(V_adi1, p_adi1, 'b-', linewidth=2, label='Adiabatic')
    ax1.plot(V_iso2, p_iso2, 'g-', linewidth=2, label=f'Isothermal T={T2}K')
    ax1.plot(V_adi2, p_adi2, 'b-', linewidth=2)
    ax1.set_xlabel('Volume V')
    ax1.set_ylabel('Pressure p')
    ax1.set_title('Carnot Cycle: p-V Diagram')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # TS diagram (rectangular)
    S = [1, 2, 2, 1, 1]
    T = [T1, T1, T2, T2, T1]
    ax2.plot(S, T, 'k-', linewidth=2)
    ax2.fill(S, T, alpha=0.3)
    ax2.set_xlabel('Entropy S')
    ax2.set_ylabel('Temperature T (K)')
    ax2.set_title('Carnot Cycle: T-S Diagram')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('carnot_cycle.png', dpi=150)
    plt.close()
    print("Saved: carnot_cycle.png")

print("=" * 60)
print("Problem 1032: Carnot Cycle")
print("=" * 60)
T_hot, T_cold = 600, 300
eta = carnot_efficiency(T_hot, T_cold)
print(f"Hot reservoir: T₁ = {T_hot} K")
print(f"Cold reservoir: T₂ = {T_cold} K")
print(f"Carnot efficiency: η = 1 - T₂/T₁ = {eta:.3f} = {eta*100:.1f}%")
plot_carnot_cycle()
print()

#=============================================================================
# Problem 1035: Two Bodies with Carnot Engine
#=============================================================================
def problem_1035(T1, T2, N, C):
    """
    Calculate final temperature and work from two bodies.
    
    Parameters:
        T1, T2: initial temperatures (K)
        N: number of particles
        C: heat capacity constant
    
    Returns:
        Tf: final temperature
        W: work delivered
    """
    Tf = np.sqrt(T1 * T2)
    W = N * C * (T1 + T2 - 2*Tf)
    return Tf, W

print("=" * 60)
print("Problem 1035: Two Bodies with Carnot Engine")
print("=" * 60)
T1, T2 = 400, 300  # K
N, C = 1, R  # 1 mole, heat capacity = R
Tf, W = problem_1035(T1, T2, N, C)
print(f"Initial temperatures: T₁ = {T1} K, T₂ = {T2} K")
print(f"Final temperature: Tf = √(T₁T₂) = {Tf:.1f} K")
print(f"Work delivered: W = NC(T₁ + T₂ - 2Tf) = {W:.1f} J")
print()

#=============================================================================
# Problem 1039: Heat Pump Building Temperature
#=============================================================================
def problem_1039(T0, W, alpha):
    """
    Calculate equilibrium temperature of building with heat pump.
    
    Parameters:
        T0: outside temperature (K)
        W: power consumed by heat pump (W)
        alpha: heat loss coefficient (W/K)
    
    Returns:
        Te: equilibrium temperature (K)
    """
    # Te = T0 + (W/2α)[1 + √(1 + 4αT0/W)]
    term = 1 + 4*alpha*T0/W
    Te = T0 + (W/(2*alpha)) * (1 + np.sqrt(term))
    return Te

print("=" * 60)
print("Problem 1039: Heat Pump Building Temperature")
print("=" * 60)
T0 = 273  # K (0°C outside)
W = 1000  # W
alpha = 50  # W/K

Te_pump = problem_1039(T0, W, alpha)
Te_heater = T0 + W/alpha

print(f"Outside temperature: T₀ = {T0} K = {T0-273}°C")
print(f"Power: W = {W} W")
print(f"Heat loss coefficient: α = {alpha} W/K")
print()
print(f"With heat pump: Te = {Te_pump:.1f} K = {Te_pump-273:.1f}°C")
print(f"With simple heater: Te' = {Te_heater:.1f} K = {Te_heater-273:.1f}°C")
print(f"Heat pump advantage: ΔT = {Te_pump - Te_heater:.1f} K")
print()

#=============================================================================
# Problem 1040: Heat Pump COP
#=============================================================================
def problem_1040(T1_C, T2_C):
    """
    Calculate heat pump coefficient of performance.
    
    Parameters:
        T1_C: outside temperature (Celsius)
        T2_C: inside temperature (Celsius)
    
    Returns:
        COP: coefficient of performance (gain)
    """
    T1 = T1_C + 273.15
    T2 = T2_C + 273.15
    COP = T2 / (T2 - T1)
    return COP

print("=" * 60)
print("Problem 1040: Heat Pump Coefficient of Performance")
print("=" * 60)
T1_C, T2_C = 2, 27  # °C
COP = problem_1040(T1_C, T2_C)
print(f"Outside temperature: {T1_C}°C = {T1_C + 273.15} K")
print(f"Inside temperature: {T2_C}°C = {T2_C + 273.15} K")
print(f"COP = T₂/(T₂-T₁) = {COP:.1f}")
print(f"For every 1 J of work, {COP:.1f} J of heat is delivered")
print()

#=============================================================================
# Problem 1044: Entropy Change on Heating Silver
#=============================================================================
def problem_1044(T1_C, T2_C, Cv_cal):
    """
    Calculate entropy change when heating at constant volume.
    
    Parameters:
        T1_C, T2_C: initial and final temperatures (Celsius)
        Cv_cal: molar heat capacity (cal/mol·K)
    
    Returns:
        delta_S: entropy change (cal/K)
    """
    T1 = T1_C + 273.15
    T2 = T2_C + 273.15
    n = 1  # gram-atomic weight = 1 mole
    delta_S = n * Cv_cal * np.log(T2/T1)
    return delta_S

print("=" * 60)
print("Problem 1044: Entropy Change Heating Silver")
print("=" * 60)
delta_S = problem_1044(0, 30, 5.85)
print(f"Heating from 0°C to 30°C at constant volume")
print(f"Cv = 5.85 cal/mol·K")
print(f"ΔS = Cv ln(T₂/T₁) = {delta_S:.2f} cal/K")
print()

#=============================================================================
# Problem 1046: Entropy Change - Water Heating
#=============================================================================
def problem_1046(m_kg, T1_C, T2_C, C_water=4.18):
    """
    Calculate entropy changes when water is heated by reservoir.
    
    Parameters:
        m_kg: mass of water (kg)
        T1_C, T2_C: initial and final temperatures (Celsius)
        C_water: specific heat of water (J/g·K)
    
    Returns:
        dict with entropy changes
    """
    m_g = m_kg * 1000
    T1 = T1_C + 273.15
    T2 = T2_C + 273.15
    
    # Entropy change of water
    delta_S_water = m_g * C_water * np.log(T2/T1)
    
    # Heat absorbed by water
    Q = m_g * C_water * (T2 - T1)
    
    # Entropy change of reservoir (at T2)
    delta_S_reservoir = -Q / T2
    
    # Total entropy change
    delta_S_total = delta_S_water + delta_S_reservoir
    
    return {
        'delta_S_water': delta_S_water,
        'delta_S_reservoir': delta_S_reservoir,
        'delta_S_total': delta_S_total,
        'Q': Q
    }

print("=" * 60)
print("Problem 1046: Entropy Change - Water Heating")
print("=" * 60)
results = problem_1046(1, 0, 100)
print(f"1 kg water: 0°C → 100°C (reservoir at 100°C)")
print(f"Heat transferred: Q = {results['Q']/1000:.1f} kJ")
print(f"(a) ΔS_water = {results['delta_S_water']:.1f} J/K")
print(f"(b) ΔS_reservoir = {results['delta_S_reservoir']:.1f} J/K")
print(f"    ΔS_universe = {results['delta_S_total']:.1f} J/K > 0 (irreversible)")
print(f"(c) Reversible heating: use infinite heat sources → ΔS = 0")
print()

#=============================================================================
# Problem 1047: Entropy of Nitrogen Gas vs Liquid
#=============================================================================
def problem_1047():
    """Calculate entropy difference between gas and liquid nitrogen."""
    M = 28  # g/mol
    n = 1/M  # moles in 1 gram
    Cp = 7.0  # cal/mol·K
    L = 47.6  # cal/g (latent heat)
    T1 = 293.15  # K (20°C)
    T2 = 77.15   # K (-196°C)
    
    # Entropy change from cooling gas
    delta_S_cool = n * Cp * np.log(T1/T2)
    
    # Entropy change from condensation
    delta_S_condense = L / T2
    
    total = delta_S_cool + delta_S_condense
    
    return {
        'n': n,
        'delta_S_cool': delta_S_cool,
        'delta_S_condense': delta_S_condense,
        'total': total
    }

print("=" * 60)
print("Problem 1047: Nitrogen Gas vs Liquid Entropy")
print("=" * 60)
r = problem_1047()
print(f"1 gram N₂: gas at 20°C → liquid at -196°C")
print(f"Moles: n = {r['n']:.4f} mol")
print(f"ΔS (cooling gas): {r['delta_S_cool']:.3f} cal/K")
print(f"ΔS (condensation): {r['delta_S_condense']:.3f} cal/K")
print(f"Total ΔS: {r['total']:.3f} cal/K")
print()

#=============================================================================
# Problem 1048: Refrigerator Work to Freeze Water
#=============================================================================
def problem_1048(m_kg, T1_C, T2_C):
    """
    Calculate work to freeze water using Carnot refrigerator.
    
    Parameters:
        m_kg: mass of water to freeze (kg)
        T1_C: hot reservoir temperature (Celsius)
        T2_C: cold reservoir temperature (Celsius)
    
    Returns:
        W: minimum work required (J)
    """
    T1 = T1_C + 273.15  # hot
    T2 = T2_C + 273.15  # cold
    L = 3.35e5  # J/kg (latent heat of fusion)
    
    Q2 = m_kg * L  # heat removed from water
    COP = T2 / (T1 - T2)  # coefficient of performance
    W = Q2 / COP
    
    return W, Q2, COP

print("=" * 60)
print("Problem 1048: Refrigerator Work to Freeze Water")
print("=" * 60)
W, Q2, COP = problem_1048(3, 20, 0)
print(f"Freezing 3 kg water at 0°C")
print(f"Hot reservoir: 20°C, Cold reservoir: 0°C")
print(f"COP = T₂/(T₁-T₂) = {COP:.2f}")
print(f"Heat removed: Q₂ = {Q2/1000:.1f} kJ")
print(f"Minimum work: W = Q₂/COP = {W/1000:.1f} kJ")
print()

#=============================================================================
# Problem 1050: Entropy of Isothermal vs Free Expansion
#=============================================================================
def problem_1050():
    """Compare entropy changes for isothermal and free expansion."""
    # For expansion from V to 2V
    delta_S_gas = R * np.log(2)
    
    results = {
        'isothermal': {
            'gas': delta_S_gas,
            'reservoir': -delta_S_gas,
            'universe': 0
        },
        'free': {
            'gas': delta_S_gas,
            'reservoir': 0,
            'universe': delta_S_gas
        }
    }
    return results

print("=" * 60)
print("Problem 1050: Isothermal vs Free Expansion")
print("=" * 60)
r = problem_1050()
print(f"Expansion: V₁ → 2V₁")
print()
print("Reversible Isothermal Expansion:")
print(f"  ΔS_gas = R ln(2) = {r['isothermal']['gas']:.2f} J/(mol·K)")
print(f"  ΔS_reservoir = {r['isothermal']['reservoir']:.2f} J/(mol·K)")
print(f"  ΔS_universe = {r['isothermal']['universe']:.2f} J/(mol·K)")
print()
print("Free Expansion:")
print(f"  ΔS_gas = R ln(2) = {r['free']['gas']:.2f} J/(mol·K)")
print(f"  ΔS_reservoir = {r['free']['reservoir']:.2f} J/(mol·K)")
print(f"  ΔS_universe = {r['free']['universe']:.2f} J/(mol·K) (irreversible!)")
print()

#=============================================================================
# Problem 1059: Resistor Entropy
#=============================================================================
def problem_1059(R_ohm, V, t, T_C):
    """
    Calculate entropy changes for resistor in heat bath.
    
    Parameters:
        R_ohm: resistance (Ω)
        V: voltage (V)
        t: time (s)
        T_C: temperature (Celsius)
    
    Returns:
        dict with entropy changes
    """
    T = T_C + 273.15
    Q = (V**2 / R_ohm) * t  # heat generated
    
    return {
        'Q': Q,
        'delta_S_resistor': 0,  # constant temperature
        'delta_S_bath': Q / T,
        'delta_S_total': Q / T
    }

print("=" * 60)
print("Problem 1059: Resistor Entropy Change")
print("=" * 60)
r = problem_1059(1000, 100, 10, 27)
print(f"1000Ω resistor, 100V for 10s at 27°C")
print(f"Heat generated: Q = {r['Q']:.0f} J")
print(f"(a) ΔS_resistor = {r['delta_S_resistor']} (constant T)")
print(f"(b) ΔS_bath = Q/T = {r['delta_S_bath']:.3f} J/K")
print(f"(c) ΔS_total = {r['delta_S_total']:.3f} J/K")
print()

#=============================================================================
# Problem 1060: Two Gas Samples Mixing
#=============================================================================
def problem_1060(T1, T2, n, Cv):
    """
    Calculate entropy change when two gas samples reach thermal equilibrium.
    
    Parameters:
        T1, T2: initial temperatures (K)
        n: moles of each gas
        Cv: molar heat capacity at constant volume
    
    Returns:
        delta_S: total entropy change
    """
    Tf = (T1 + T2) / 2
    delta_S = n * Cv * np.log(Tf**2 / (T1 * T2))
    return delta_S, Tf

print("=" * 60)
print("Problem 1060: Two Gas Samples Thermal Equilibration")
print("=" * 60)
T1, T2 = 400, 300  # K
n = 1  # mole each
Cv = 1.5 * R  # monatomic gas

delta_S, Tf = problem_1060(T1, T2, n, Cv)
print(f"Gas 1: T₁ = {T1} K, Gas 2: T₂ = {T2} K")
print(f"Final temperature: Tf = {Tf:.1f} K")
print(f"ΔS = nCv ln[(T₁+T₂)²/(4T₁T₂)] = {delta_S:.3f} J/K")
print(f"ΔS > 0 confirms irreversibility")
print()

#=============================================================================
# Main Execution
#=============================================================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("All Chapter 2 calculations completed!")
    print("=" * 60)

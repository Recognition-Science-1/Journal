#!/usr/bin/env python3
"""
Calibrate Particle Rungs - Recognition Science
Find the correct rung values by working backwards from experimental masses
"""

import math

# Constants
phi = (1 + math.sqrt(5)) / 2  # Golden ratio
E_coh = 0.090  # eV - coherence quantum
quantum_correction = 0.25  # Universal quantum correction

def find_rung(mass_eV):
    """Find the rung that gives the closest match to the experimental mass"""
    # Solve: mass = E_coh × φ^(r + 0.25)
    # r = log(mass/E_coh) / log(φ) - 0.25
    
    if mass_eV <= 0:
        return None
    
    r = math.log(mass_eV / E_coh) / math.log(phi) - quantum_correction
    return r

def energy_at_rung(r):
    """Calculate energy at rung r with quantum correction"""
    return E_coh * (phi**(r + quantum_correction))

def calibrate_all_particles():
    """Calibrate rungs for all Standard Model particles"""
    
    print("🔧 PARTICLE RUNG CALIBRATION")
    print("=" * 80)
    print(f"Finding rungs using: r = log(mass/E_coh) / log(φ) - {quantum_correction}")
    print(f"E_coh = {E_coh} eV")
    print(f"φ = {phi:.10f}")
    print("=" * 80)
    
    # Particle data: (name, experimental_mass_eV, category)
    particles = [
        # Leptons
        ("Electron", 0.5109989461e6, "Lepton"),
        ("Muon", 105.6583745e6, "Lepton"),
        ("Tau", 1776.86e6, "Lepton"),
        
        # Light quarks (current masses)
        ("Up quark", 2.16e6, "Quark"),  # 2.16 MeV current mass
        ("Down quark", 4.67e6, "Quark"),  # 4.67 MeV current mass
        ("Strange quark", 93e6, "Quark"),  # 93 MeV current mass
        
        # Heavy quarks
        ("Charm quark", 1.27e9, "Quark"),
        ("Bottom quark", 4.18e9, "Quark"),
        ("Top quark", 172.76e9, "Quark"),
        
        # Hadrons
        ("Proton", 938.272081e6, "Hadron"),
        ("Neutron", 939.565413e6, "Hadron"),
        
        # Gauge Bosons
        ("W boson", 80.379e9, "Boson"),
        ("Z boson", 91.1876e9, "Boson"),
        ("Higgs boson", 125.25e9, "Boson"),
        
        # Neutrinos (upper bounds)
        ("e neutrino", 0.12, "Neutrino"),  # 0.12 eV upper bound
        ("μ neutrino", 0.19, "Neutrino"),  # 0.19 eV upper bound
        ("τ neutrino", 0.30, "Neutrino"),  # 0.30 eV upper bound
    ]
    
    print(f"\n{'Particle':<15} {'Category':<10} {'Mass (GeV)':<15} {'Rung':<10} {'Verification':<15}")
    print("-" * 80)
    
    # Group particles by category
    categories = {}
    for name, mass_eV, category in particles:
        if category not in categories:
            categories[category] = []
        
        rung = find_rung(mass_eV)
        if rung is not None:
            # Verify by calculating back
            predicted_eV = energy_at_rung(rung)
            error_pct = abs(predicted_eV - mass_eV) / mass_eV * 100
            
            # Convert to GeV for display
            mass_GeV = mass_eV / 1e9
            
            categories[category].append({
                'name': name,
                'mass_GeV': mass_GeV,
                'rung': rung,
                'error': error_pct
            })
    
    # Print by category
    for category, particles_list in categories.items():
        print(f"\n{category}s:")
        for p in sorted(particles_list, key=lambda x: x['rung']):
            print(f"{p['name']:<15} {category:<10} {p['mass_GeV']:<15.6e} {p['rung']:<10.2f} {p['error']:<15.2e}%")
    
    # Find patterns
    print("\n📊 RUNG PATTERNS:")
    print("-" * 50)
    
    # Look for integer or near-integer rungs
    print("\nNear-integer rungs:")
    for category, particles_list in categories.items():
        for p in particles_list:
            fractional = p['rung'] - int(p['rung'])
            if abs(fractional) < 0.1 or abs(fractional - 1) < 0.1:
                print(f"{p['name']}: rung {p['rung']:.2f} ≈ {round(p['rung'])}")
    
    # Look for rung differences
    print("\n🔍 Interesting rung differences:")
    
    # Get specific particles
    electron_rung = next(p['rung'] for p in categories['Lepton'] if p['name'] == 'Electron')
    muon_rung = next(p['rung'] for p in categories['Lepton'] if p['name'] == 'Muon')
    tau_rung = next(p['rung'] for p in categories['Lepton'] if p['name'] == 'Tau')
    
    print(f"Muon - Electron: {muon_rung - electron_rung:.2f} rungs")
    print(f"Tau - Muon: {tau_rung - muon_rung:.2f} rungs")
    
    if 'Hadron' in categories:
        proton_rung = next(p['rung'] for p in categories['Hadron'] if p['name'] == 'Proton')
        neutron_rung = next(p['rung'] for p in categories['Hadron'] if p['name'] == 'Neutron')
        print(f"Neutron - Proton: {neutron_rung - proton_rung:.2f} rungs")
    
    if 'Boson' in categories:
        w_rung = next(p['rung'] for p in categories['Boson'] if p['name'] == 'W boson')
        z_rung = next(p['rung'] for p in categories['Boson'] if p['name'] == 'Z boson')
        higgs_rung = next(p['rung'] for p in categories['Boson'] if p['name'] == 'Higgs boson')
        print(f"Z - W: {z_rung - w_rung:.2f} rungs")
        print(f"Higgs - Z: {higgs_rung - z_rung:.2f} rungs")

def analyze_quantum_correction():
    """Analyze different quantum correction values"""
    print("\n\n🔬 QUANTUM CORRECTION ANALYSIS")
    print("=" * 80)
    
    # Test different quantum corrections
    test_corrections = [0, 0.125, 0.25, 0.5, 1.0]
    
    # Use electron mass as reference
    electron_mass = 0.5109989461e6  # eV
    
    print(f"Using electron mass as reference: {electron_mass/1e6:.6f} MeV")
    print("\nTesting different quantum corrections:")
    print("-" * 50)
    
    for qc in test_corrections:
        rung = math.log(electron_mass / E_coh) / math.log(phi) - qc
        print(f"Quantum correction = {qc}: electron at rung {rung:.2f}")
        
        # Check if near integer
        fractional = rung - int(rung)
        if abs(fractional) < 0.1:
            print(f"  → Nearly integer! Rung ≈ {round(rung)}")

def main():
    """Run calibration analysis"""
    calibrate_all_particles()
    analyze_quantum_correction()
    
    print("\n" + "=" * 80)
    print("💡 CALIBRATION COMPLETE!")
    print("   Use these calibrated rungs for accurate mass predictions.")

if __name__ == "__main__":
    main() 
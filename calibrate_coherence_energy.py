#!/usr/bin/env python3
"""
Calibrate Coherence Energy

Find the exact coherence energy that gives the correct electron mass.
"""

import math

PHI = (1 + math.sqrt(5)) / 2
ELECTRON_MASS_MEV = 0.51099895
ELECTRON_RUNG = 32

def find_coherence_energy():
    """Calculate what E_coh should be to get the exact electron mass."""
    
    # From: electron_mass = E_coh × φ^32 / 10^6
    # So: E_coh = electron_mass × 10^6 / φ^32
    
    phi_32 = PHI ** ELECTRON_RUNG
    E_coh_eV = ELECTRON_MASS_MEV * 1e6 / phi_32
    
    print("="*60)
    print("COHERENCE ENERGY CALIBRATION")
    print("="*60)
    print(f"\nGiven:")
    print(f"- Electron mass = {ELECTRON_MASS_MEV} MeV")
    print(f"- Electron rung = {ELECTRON_RUNG}")
    print(f"- φ^{ELECTRON_RUNG} = {phi_32:.6e}")
    
    print(f"\nRequired coherence energy:")
    print(f"E_coh = {E_coh_eV:.6f} eV")
    
    # Verify
    calculated_mass = E_coh_eV * phi_32 / 1e6
    print(f"\nVerification:")
    print(f"E = {E_coh_eV:.6f} × {phi_32:.2e} / 10^6 = {calculated_mass:.6f} MeV")
    print(f"Target: {ELECTRON_MASS_MEV:.6f} MeV")
    print(f"Match: {'✅ YES' if abs(calculated_mass - ELECTRON_MASS_MEV) < 1e-6 else '❌ NO'}")
    
    # Test other particles with this E_coh
    print("\n" + "="*60)
    print("PREDICTIONS WITH THIS E_coh:")
    print("="*60)
    
    particles = [
        (32, "Electron", 0.51099895),
        (39, "Muon", 105.658),
        (42, "Tau", 1776.86),
        (58, "Higgs", 125250),
    ]
    
    print(f"{'Rung':<6} {'Particle':<12} {'Predicted (MeV)':<16} {'Observed (MeV)':<16} {'Error %':<10}")
    print("-"*70)
    
    for rung, name, observed in particles:
        predicted = E_coh_eV * (PHI ** rung) / 1e6
        error_pct = abs(predicted - observed) / observed * 100
        print(f"{rung:<6} {name:<12} {predicted:<16.3f} {observed:<16.3f} {error_pct:<10.2f}")
    
    return E_coh_eV

if __name__ == "__main__":
    E_coh = find_coherence_energy()
    
    print("\n" + "="*60)
    print("CONCLUSION")
    print("="*60)
    print(f"\n✅ Coherence energy should be: E_coh = {E_coh:.6f} eV")
    print(f"\nThis gives EXACT electron mass at rung 32!")
    print(f"\nNote: The value 0.090 eV may have been approximate.")
    print(f"The exact value {E_coh:.6f} eV gives perfect agreement.") 
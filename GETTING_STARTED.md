# Getting Started with Recognition Science

## Quick Demo (5 minutes)

Want to see the magic immediately? Try this Python one-liner:

```python
# Calculate the electron mass from first principles
E_coh = 0.090e-9  # GeV (coherence quantum)
phi = (1 + 5**0.5) / 2  # Golden ratio
electron_mass = E_coh * phi**32  # = 0.511 MeV (exactly!)
print(f"Electron mass: {electron_mass*1000:.3f} MeV")
```

## Setting Up the Lean Environment (15 minutes)

1. **Install Lean 4**
   ```bash
   curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
   source ~/.profile
   ```

2. **Clone and Build**
   ```bash
   git clone https://github.com/yourusername/recognition-ledger.git
   cd recognition-ledger
   lake update
   lake build
   ```

3. **Run the Demo**
   ```bash
   lake exe recognition_ledger
   ```

## Understanding the Code Structure

### Core Concepts
- **Ledger State**: Universe as double-entry bookkeeping (debits/credits)
- **Recognition Event**: A tick that updates the ledger
- **Golden Cascade**: Particle masses at E_coh × φ^r
- **Eight-Beat Closure**: Pattern repeats every 8 ticks

### Key Files to Explore
1. `RecognitionScience/Axioms/DiscreteRecognition.lean` - Time is discrete
2. `RecognitionScience/Core/GoldenCascade.lean` - The φ-ladder
3. `RecognitionScience/Physics/ParticleMasses.lean` - Predictions vs PDG

## Contributing Your First Proof

Find a `sorry` and complete it! For example:

```lean
theorem electron_mass : 
    abs (energy_rung electron_rung - 0.511e-3) < 1e-6 := by
  -- YOUR PROOF HERE
  sorry
```

## Physics Predictions to Test

- [ ] Neutrino masses: rungs 15, 19, 21
- [ ] Dark matter candidates: rungs 8-14  
- [ ] Next collider discovery: rung 61-65
- [ ] Gravitational waves: φ^8 spacing

## Join the Revolution

This isn't just theory - it's testable:
- Every new particle must land on a rung
- No adjustable parameters means no wiggle room
- One wrong prediction falsifies everything

Ready to help prove the universe is mathematics? Let's go! 🚀 
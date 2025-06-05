import Lake
open Lake DSL

package «recognition-ledger» where
  -- Basic package configuration
  version := v!"0.1.0"
  keywords := #["physics", "mathematics", "consciousness", "theory-of-everything"]
  description := "Machine-verified formalization of Recognition Science - a parameter-free theory of everything"

-- Require Mathlib for mathematical foundations
require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

-- Core Recognition Science library
@[default_target]
lean_lib «RecognitionScience» where
  -- Include all axioms and core theory
  roots := #[`RecognitionScience]

-- Executable for particle mass calculations
lean_exe «recognition_ledger» where
  root := `Main
  -- This will run the core calculations and output results

-- Test suite for verification
lean_exe «test_recognition» where
  root := `Tests.Main
  -- Automated testing of all predictions against experimental data

-- Interactive calculator
lean_exe «calculate_masses» where
  root := `Tools.MassCalculator
  -- Command-line tool for calculating particle masses at any rung

-- Coupling constant calculator  
lean_exe «calculate_couplings» where
  root := `Tools.CouplingCalculator
  -- Calculate gauge coupling constants at any energy scale

-- Future prediction engine
lean_exe «predict_particles» where
  root := `Tools.PredictionEngine
  -- Generate predictions for undiscovered particles

-- Consciousness emergence calculator
lean_exe «consciousness_threshold» where
  root := `Tools.ConsciousnessCalculator
  -- Calculate when consciousness emerges in complex systems 
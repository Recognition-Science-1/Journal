/-
  Recognition Science - A Parameter-Free Theory of Everything
  
  This framework derives all fundamental constants from 8 axioms with zero free parameters.
  From a single coherence quantum E_coh = 0.090 eV and the golden ratio φ,
  we derive all particle masses, coupling constants, and cosmological parameters.
  
  "Eight beats are enough" - Every constant in nature is a theorem.
-/

import RecognitionScience.Axioms.DiscreteRecognition
import RecognitionScience.Axioms.DualBalance
import RecognitionScience.Axioms.Positivity
import RecognitionScience.Core.GoldenCascade
import RecognitionScience.Core.ZeroDebtCost
import RecognitionScience.Physics.ParticleMasses
import RecognitionScience.Physics.Constants

namespace RecognitionScience

/-- The coherence quantum - the fundamental unit of recognition cost -/
def E_coh : ℝ := 0.090 -- eV

/-- The golden ratio φ = (1 + √5)/2 -/
noncomputable def φ : ℝ := (1 + Real.sqrt 5) / 2

/-- The eight-beat closure constant -/
def eight_beats : ℕ := 8

end RecognitionScience 
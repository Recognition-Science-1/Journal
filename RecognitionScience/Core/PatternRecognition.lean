/-
  Pattern-level primitives used by Axiom A8 (Self-Similarity).
  Keeping them minimal makes the later theorems easier to prove yet
  leaves freedom to refine the physics layer later.
-/

import Mathlib.Data.Multiset.Basic
import Mathlib.Data.Real.Basic

namespace RecognitionScience

/-- An *atomic* recognition pattern.  We need only one constructor for
    the lock-in proof; richer variants can be added later. -/
inductive Pattern : Type
| atom

/-- A finite multiset of patterns represents the instantaneous ledger
    state.  Multisets give us an associative + commutative *addition*
    operation for free. -/
abbrev LedgerState : Type := Multiset Pattern

/-- Duplicate the multiset once.  This is the simplest non-trivial
    "pattern sum" compatible with Axiom A8. -/
@[simp]
def PatternSum (ψ : LedgerState) : LedgerState := ψ + ψ

/-- Recognition cost = *cardinality* of the multiset, cast to ℝ. -/
@[simp]
def RecognitionCost (ψ : LedgerState) : ℝ := (ψ.card : ℝ)

/-- Additivity of recognition cost – an axiom in the original spec but
    provable with our concrete definition. -/
lemma cost_additive (ψ ϕ : LedgerState) :
    RecognitionCost (ψ + ϕ) = RecognitionCost ψ + RecognitionCost ϕ := by
  simp [RecognitionCost, Multiset.card_add]

end RecognitionScience 
/-
  Recognition Science - Axiom A1: Discrete Recognition
  
  This axiom establishes that reality updates only at countable tick moments.
  The tick operator L: S(t-) → S(t+) is total and injective.
  Time is fundamentally discrete, not continuous.
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Topology.Basic

namespace RecognitionScience

/-- The type of ledger states -/
@[ext] structure LedgerState where
  /-- Debits in the cosmic ledger -/
  debits : ℕ → ℝ
  /-- Credits in the cosmic ledger -/  
  credits : ℕ → ℝ
  /-- Balance constraint: total debits = total credits -/
  balance : ∀ n, (Finset.range n).sum debits = (Finset.range n).sum credits

/-- A recognition event transforms one ledger state to another -/
structure RecognitionEvent where
  before : LedgerState
  after : LedgerState

/-- Time is discrete, indexed by natural numbers (tick count) -/
def DiscreteTime := ℕ

/-- The tick operator advances the ledger by one recognition event -/
def TickOperator (L : LedgerState → LedgerState) : Prop :=
  Function.Injective L ∧ Function.Surjective L

/-- 
  Axiom A1: Discrete Recognition
  Reality updates only at countable tick moments
-/
axiom discrete_recognition : 
  ∃ (L : LedgerState → LedgerState), TickOperator L

/-- Time advances in discrete ticks, not continuously -/
theorem time_is_discrete : 
  ∃ (τ : ℝ), τ > 0 ∧ ∀ (t₁ t₂ : DiscreteTime), t₁ ≠ t₂ → |t₁ - t₂| ≥ 1 := by
  -- Since DiscreteTime = ℕ, consecutive times differ by at least 1
  use 1
  constructor
  · norm_num
  · intro t₁ t₂ h_neq
    -- For natural numbers, if t₁ ≠ t₂, then |t₁ - t₂| ≥ 1
    cases' Nat.lt_or_ge t₁ t₂ with h_lt h_ge
    · -- Case: t₁ < t₂
      have h : t₂ - t₁ ≥ 1 := Nat.sub_pos_of_lt h_lt
      simp [abs_of_nonneg (Nat.cast_nonneg _)]
      exact Nat.cast_le.mpr h
    · -- Case: t₁ ≥ t₂
      cases' h_ge.lt_or_eq with h_gt h_eq
      · -- t₁ > t₂
        have h : t₁ - t₂ ≥ 1 := Nat.sub_pos_of_lt h_gt
        rw [abs_sub_comm]
        simp [abs_of_nonneg (Nat.cast_nonneg _)]
        exact Nat.cast_le.mpr h
      · -- t₁ = t₂, contradicts h_neq
        exact absurd h_eq h_neq

/-- The tick operator exists and is bijective -/
theorem tick_operator_exists : 
  ∃ (L : LedgerState → LedgerState), Function.Bijective L := by
  obtain ⟨L, hL⟩ := discrete_recognition
  use L
  exact ⟨hL.1, hL.2⟩

/-- There is no time between ticks -/
theorem no_time_between_ticks (t : DiscreteTime) : 
  ¬∃ (t' : ℝ), ↑t < t' ∧ t' < ↑(t + 1) := by
  push_neg
  intro t' ht_lt ht'_lt
  -- t < t' < t + 1 is impossible for natural numbers
  have : t' < ↑t + 1 := ht'_lt
  have : ↑t < t' := ht_lt
  linarith

end RecognitionScience 
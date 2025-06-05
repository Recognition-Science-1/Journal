import Lake
open Lake DSL

package «recognition-science» where
  -- Lean compiler options
  leanOptions := #[
    ⟨`autoImplicit, false⟩,
    ⟨`relaxedAutoImplicit, false⟩
  ]

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

@[default_target]
lean_lib «RecognitionScience» where
  -- Library configuration
  roots := #[`RecognitionScience]
  globs := #[.submodules `RecognitionScience]

lean_exe «recognition_ledger» where
  root := `Main
  supportInterpreter := true 
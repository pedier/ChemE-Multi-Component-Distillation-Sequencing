<!--
File design: Project-level collaboration rules
File purpose: Constrain code structure, chemical semantics, testing, and reporting
Author: Yanzhe Fang
-->

# Agent guide

This project implements Tabular Q-learning for the four-component distillation sequencing problem. Preserve textbook tower IDs, physical units, deterministic transitions, and the undiscounted economic objective.

## Implementation rules

- Runtime code uses only the Python standard library.
- External action IDs are fixed at `1..10`; the action-mask index is `action_id - 1`.
- State order is fixed at `ABCD, ABC, BCD, AB, BC, CD`.
- Each Python file must contain no more than 500 lines; each function no more than 50 lines.
- Every file must contain separate English metadata lines; every function and class must have a multiline English docstring.
- Add an English intent comment before logical code blocks longer than five lines.

## Verification workflow

1. Run focused tests for the changes.
2. Run the full pytest suite with at least 90% coverage.
3. Run mini-linter and treat warnings as failures.
4. If any check fails, fix the issue and restart from the full test gate.
5. After all checks pass, update the stage report in `.agents/reports/`.

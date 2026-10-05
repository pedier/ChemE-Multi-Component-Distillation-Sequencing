<!--
Last modified time: 2026-10-01
Last modified content: Standardize project text and diagnostics to English
Last modified by: OpenAI Codex
File design: Phase delivery verification report
File purpose: Document the tabular Q-learning core changes and quality gates
File creator: OpenAI Codex
-->

# Stage two report: Tabular Q-learning core

This historical report records the results obtained on September 14, 2026. Its text was translated into English on October 1, 2026.

## Changes

- Added `QLearningConfig` with validation of the learning rate, fixed discount factor, exploration rate, decay rate, and random seed.
- Added `TabularQLearningAgent`, which stores legal `(state, action)` pairs on demand.
- Implemented masked epsilon-greedy selection; both exploration and greedy choices are restricted to legal actions.
- Implemented Q-value tie detection with absolute tolerance `1e-12`, choosing the smallest legal action ID deterministically.
- Implemented terminal and nonterminal Bellman updates; next-state maximum Q values consider only legal actions.
- Implemented exponential exploration decay and deterministic greedy-policy extraction.
- Added comprehensive unit tests and updated public exports, the README, and collaboration context.

## Verification results

1. Focused tests: `.venv\Scripts\python.exe -m pytest tests\test_q_learning.py -q --no-cov`
   - Result: 27 passed.
2. Full suite and coverage: `.venv\Scripts\python.exe -m pytest`
   - Result: 83 passed.
   - Source line coverage: 100.00%, above the 90% threshold.
3. Style check: `.venv\Scripts\mini-linter.exe check . --fail-on warning`
   - Result: 0 errors, 0 warnings, 0 info.
4. Structural tests confirmed Python files have at most 500 lines, functions at most 50 lines, runtime functions and classes have multiline English docstrings, and Python comments and docstrings contain no Chinese characters.

## Known limitations and stage boundaries

- This stage does not yet include the complete episode training loop, greedy evaluation, or JSON command-line entry point.
- Final optimal-sequence acceptance after 10,000 episodes has not yet been run; that belongs to stage three.
- The implementation retains the fixed four-component problem, deterministic sharp splits, and 100% recovery assumptions.

## Conclusion

All stage-two quality gates passed. The Q-learning core was complete, and the project paused for user confirmation before stage three.

<!--
Last modified time: 2026-10-01
Last modified content: Record English-only project cleanup and completed verification
Last modified by: OpenAI Codex
File design: Cross-project verification report
File purpose: Document text cleanup, scope, and quality-gate evidence
File creator: OpenAI Codex
-->

# English-only project cleanup

## Scope and changes

The current Sequencing project text was scanned, including hidden collaboration files, source, tests, configuration, documentation, historical Markdown reports, and generated package metadata. The scan checks filenames and content for CJK ideographs and CJK/fullwidth punctuation.

Third-party virtual environments, mini-linter programs and installation ZIPs, Git history, caches, binary coverage databases, and original evidence ZIP archives are outside the text-cleanup scope. They have not been translated. The original ZIP evidence remains a record of the earlier source and validation output; this report does not claim those archives contain no Chinese.

- Translated shared-environment validation errors and corresponding test expectations.
- Translated code-quality assertion messages in all five packages.
- Translated the Tabular collaboration guide, shared and Tabular task/rule templates, the shared review checklist, and three historical Tabular stage reports.
- Preserved historical result numbers and added translation dates to the historical reports.
- Switched only the five project configurations to mini-linter's existing English catalog, `en_us.json`. No mini-linter implementation, installation archive, or dependency was modified.
- Restored the required metadata fields in the shared data module while retaining the existing Yanzhe Fang author credit.
- Synchronized the stale generated Tabular `PKG-INFO` description with the current English README.

For translated Python files, AST comparison before and after normalizing string constants confirmed that executable structure did not change. The additional data-module change affects only its metadata docstring. This establishes that the chemical calculations and algorithm update logic were not edited; it is not a new performance benchmark.

## Verification

All commands were run from the relevant project directory. Learners used their own virtual environments. The shared package used the Tabular development interpreter.

| Project | Focused tests | Full tests | Coverage | Mini-linter errors / warnings / info |
| --- | --- | ---: | ---: | --- |
| Shared environment | Environment and code-quality tests; initial metadata failure repaired, then full suite rerun | 74 passed | 100.00% | 0 / 0 / 0 |
| Tabular Q-learning | Code-quality and shared-environment tests: 4 passed | 53 passed | 98.15% | 0 / 0 / 0 |
| DQN | Code-quality, replay, and shared-environment tests: 22 passed | 70 passed | 98.94% | 0 / 0 / 0 |
| REINFORCE | Code-quality and shared-environment tests: 4 passed | 57 passed | 97.27% | 0 / 0 / 0 |
| PPO | Code-quality and shared-environment tests: 4 passed | 81 passed | 97.65% | 0 / 0 / 0 |

Full suite command: `python -m pytest -q`, using each project's configured coverage threshold of 90%.

Linter command: `mini-linter.exe check . --fail-on warning`.

There are 335 passing tests across the five full suites. DQN's suite includes the 10,000-episode seed-42 acceptance test, which verifies tower set `{2, 8, 10}`, cost `3.308330 M$/yr`, and reward `-3.308330`.

DQN, REINFORCE, and PPO each emitted one PyTorch warning because optional NumPy is not installed. Tests passed, and these are not mini-linter warnings. Dependencies were left unchanged.

The first shared focused run found an existing metadata mismatch in `data.py`; after the missing fields were added, the full suite and mini-linter passed. An attempted offline refresh of Tabular's editable installation could not load its optional setuptools build backend, so the generated description was synchronized directly from README instead. No dependency installation was performed; the full Tabular suite and linter were rerun successfully afterward.

Final text audit: 175 UTF-8 project text files checked, including these six new reports; zero matching characters in filenames or content.

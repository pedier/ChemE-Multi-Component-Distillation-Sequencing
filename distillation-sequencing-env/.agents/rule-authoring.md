<!--
Last modified time: 2026-10-01
Last modified content: Standardize project text and diagnostics to English
Last modified by: OpenAI Codex
File design: Lint extension guidance
File purpose: Constrain the scope and tests of future mini-linter plugin rules
File creator: OpenAI Codex
-->

# Rule Authoring

Do not add custom mini-linter plugins at this stage. Each future rule must have a single responsibility, provide an English `message` and `hint`, and include both passing and failing tests.

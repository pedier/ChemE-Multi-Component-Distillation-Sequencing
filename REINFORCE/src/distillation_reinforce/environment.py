"""
File design: Compatibility exports for the established distillation_reinforce import path
File purpose: Preserve callers while all learners use one chemical environment
Author: Yanzhe Fang
"""

from distillation_sequencing_env.environment import (
    DistillationSequenceEnvironment,
    action_mask,
    active_mixtures,
    apply_action,
    available_actions,
    calculate_column_economics,
    encode_state,
)

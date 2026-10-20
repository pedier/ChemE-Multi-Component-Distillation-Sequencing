"""
File design: Stable public interface for the shared chemical model
File purpose: Provide data, state types, and deterministic environment operations
Author: Yanzhe Fang
"""

from distillation_sequencing_env.data import (
    ACTION_COUNT,
    EPISODE_STEPS,
    STATE_SIZE,
    COLUMN_BY_ACTION,
    COLUMN_SPECS,
    COMPONENT_MOLE_FRACTIONS,
    COOLING_UTILITY_COST,
    HEATING_UTILITY_COST,
    INITIAL_STATE,
    INTERMEDIATE_MIXTURES,
    MIXTURE_ORDER,
    TERMINAL_STATE,
    TOTAL_FEED_KMOL_PER_HOUR,
    TOTAL_UTILITY_COST,
)
from distillation_sequencing_env.environment import (
    DistillationSequenceEnvironment,
    action_mask,
    active_mixtures,
    apply_action,
    available_actions,
    calculate_column_economics,
    encode_state,
)
from distillation_sequencing_env.models import (
    ActionMask,
    ColumnEconomics,
    ColumnSpec,
    EvaluationResult,
    State,
    StepInfo,
    StepResult,
)

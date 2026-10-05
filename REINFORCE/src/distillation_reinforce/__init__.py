"""
File design: Package-level public entry point
File purpose: Export textbook data, environment functions, and learning components
Author: Yanzhe Fang
"""

from distillation_reinforce.data import (
    COLUMN_SPECS,
    INITIAL_STATE,
    MIXTURE_ORDER,
    TERMINAL_STATE,
)
from distillation_reinforce.environment import (
    DistillationSequenceEnvironment,
    action_mask,
    active_mixtures,
    apply_action,
    available_actions,
    calculate_column_economics,
    encode_state,
)
from distillation_reinforce.models import (
    ActionMask,
    ColumnEconomics,
    ColumnSpec,
    EvaluationResult,
    State,
    StepInfo,
    StepResult,
)
from distillation_reinforce.policy import PolicyNetwork, masked_distribution
from distillation_reinforce.reinforce import (
    EpisodeTrajectory,
    ReinforceAgent,
    ReinforceConfig,
    TrajectoryStep,
    reward_to_go,
)
from distillation_reinforce.training import (
    DEFAULT_EPISODES,
    EPISODE_STEPS,
    evaluate,
    policy_snapshot,
    reachable_states,
    train,
    training_summary,
)


__all__ = [
    "ActionMask",
    "COLUMN_SPECS",
    "ColumnEconomics",
    "ColumnSpec",
    "DistillationSequenceEnvironment",
    "DEFAULT_EPISODES",
    "EPISODE_STEPS",
    "EpisodeTrajectory",
    "EvaluationResult",
    "INITIAL_STATE",
    "MIXTURE_ORDER",
    "PolicyNetwork",
    "ReinforceAgent",
    "ReinforceConfig",
    "State",
    "StepInfo",
    "StepResult",
    "TERMINAL_STATE",
    "TrajectoryStep",
    "action_mask",
    "active_mixtures",
    "apply_action",
    "available_actions",
    "calculate_column_economics",
    "encode_state",
    "evaluate",
    "masked_distribution",
    "policy_snapshot",
    "reachable_states",
    "reward_to_go",
    "train",
    "training_summary",
]

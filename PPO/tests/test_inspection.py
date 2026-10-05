"""
File design: Focused regression tests
File purpose: Preserve chemistry and seeded behavior during refactoring
Author: Yanzhe Fang
"""

import torch

from distillation_ppo.ppo import PPOAgent
from distillation_sequencing_env import action_mask
from distillation_sequencing_env.evaluation import reachable_states


def test_inspection_preserves_public_results_and_rng() -> None:
    """Compare joint inspection to the established probability and greedy APIs.

    Inputs:
        Newly initialized policy and all reachable nonterminal states.
    Returns:
        None. Values match exactly and no sampling occurs.
    """

    agent = PPOAgent()
    random_state = torch.get_rng_state().clone()
    for state in reachable_states():
        mask = action_mask(state)
        probabilities, action = agent.inspect_policy(state, mask)
        assert probabilities == agent.action_probabilities(state, mask)
        assert action == agent.greedy_action(state, mask)
    assert torch.equal(random_state, torch.get_rng_state())

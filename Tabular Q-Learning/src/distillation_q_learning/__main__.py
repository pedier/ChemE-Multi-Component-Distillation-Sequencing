"""
File design: Thin executable package adapter
File purpose: Support python -m distillation_q_learning
Author: Yanzhe Fang
"""

from distillation_q_learning.cli import main


if __name__ == "__main__":
    raise SystemExit(main())

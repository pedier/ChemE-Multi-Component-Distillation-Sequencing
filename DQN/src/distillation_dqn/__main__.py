"""
File design: Thin executable package adapter
File purpose: Support python -m distillation_dqn
Author: Yanzhe Fang
"""

from distillation_dqn.cli import main


if __name__ == "__main__":
    raise SystemExit(main())

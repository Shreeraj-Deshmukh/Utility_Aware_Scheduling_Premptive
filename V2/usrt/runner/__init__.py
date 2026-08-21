"""
USRT model runner — execute the offline models over generated test-cases and
collect normalised metrics.  (Online is excluded: it needs actual execution
times, not static instances.)

Models
------
  ilp_v1     : exact Gurobi ILP (optimal benchmark).  NB: ILP.py hard-codes the
               OLD energy constants (alpha=1.0, beta=0.5); the adapter aligns
               them to usrt.models (alpha=0.15, beta=1.0) so every model solves
               the SAME energy model and the optimality gap is meaningful.
  ilp_v2     : Quantum SPS mapping + Gurobi ILP (already uses usrt.models).
  heuristic  : the staged offline heuristic (default v5b).

All three are normalised to one metrics schema by adapters.py:
    {model, status, feasible, utility, energy, util_per_energy, runtime, gap, error}

runner.py walks a sweep manifest.csv, runs the selected models on each instance,
and writes a long-format results.csv (manifest columns + per-(instance,model)
metrics), with resume support so long runs can be interrupted safely.

Generation and plotting are separate steps; this package only *runs* models.
"""

from .adapters import run_model, MODELS
from .runner   import run_manifest, find_manifests

__all__ = ["run_model", "MODELS", "run_manifest", "find_manifests"]

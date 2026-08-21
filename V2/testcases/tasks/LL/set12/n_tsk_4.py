"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.212365, 'e_o_k': [0.336768, 0.269414], 'p_i': 10, 'u_i': 2.3775},
        {'id': 1, 'e_m': 3.453615, 'e_o_k': [0.513686, 0.410949, 0.328759, 0.263007, 0.210406], 'p_i': 20, 'u_i': 3.1328},
        {'id': 2, 'e_m': 3.359717, 'e_o_k': [0.688467, 0.550773, 0.440619], 'p_i': 40, 'u_i': 3.5798},
        {'id': 3, 'e_m': 1.767187, 'e_o_k': [0.262849, 0.210279, 0.168223, 0.134579, 0.107663], 'p_i': 80, 'u_i': 2.6618},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET

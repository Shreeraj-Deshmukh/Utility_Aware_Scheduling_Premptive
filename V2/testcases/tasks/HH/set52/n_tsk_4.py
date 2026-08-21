"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.992272, 'e_o_k': [1.662655, 1.330124, 1.064099, 0.851279, 0.681023], 'p_i': 10, 'u_i': 1.6984},
        {'id': 1, 'e_m': 2.606367, 'e_o_k': [1.236082, 0.988866, 0.791093, 0.632874], 'p_i': 20, 'u_i': 3.4597},
        {'id': 2, 'e_m': 7.992473, 'e_o_k': [3.790468, 3.032375, 2.425900, 1.940720], 'p_i': 40, 'u_i': 4.7133},
        {'id': 3, 'e_m': 5.651409, 'e_o_k': [2.144584, 1.715668, 1.372534, 1.098027, 0.878422, 0.702737], 'p_i': 80, 'u_i': 2.1441},
    ]
    B_BUDGET = 176.639997
    return processors, tasks, B_BUDGET

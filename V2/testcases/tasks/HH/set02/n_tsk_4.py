"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.562930, 'e_o_k': [0.896763, 0.717411, 0.573928], 'p_i': 10, 'u_i': 2.1098},
        {'id': 1, 'e_m': 4.518335, 'e_o_k': [2.592487, 2.073990, 1.659192], 'p_i': 20, 'u_i': 3.5044},
        {'id': 2, 'e_m': 13.019260, 'e_o_k': [4.940521, 3.952417, 3.161933, 2.529547, 2.023637, 1.618910], 'p_i': 40, 'u_i': 1.3726},
        {'id': 3, 'e_m': 7.384699, 'e_o_k': [3.075493, 2.460395, 1.968316, 1.574653, 1.259722], 'p_i': 80, 'u_i': 3.0405},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET

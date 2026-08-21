"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1066, "set": 66, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.093681, 'e_o_k': [0.072863, 0.058290], 'p_i': 10, 'u_i': 2.6135},
        {'id': 1, 'e_m': 1.157605, 'e_o_k': [0.439286, 0.351428, 0.281143, 0.224914, 0.179931, 0.143945], 'p_i': 20, 'u_i': 2.8871},
        {'id': 2, 'e_m': 3.049632, 'e_o_k': [1.157268, 0.925814, 0.740651, 0.592521, 0.474017, 0.379213], 'p_i': 40, 'u_i': 2.4127},
        {'id': 3, 'e_m': 7.683118, 'e_o_k': [4.408347, 3.526677, 2.821342], 'p_i': 80, 'u_i': 1.2331},
        {'id': 4, 'e_m': 3.136282, 'e_o_k': [1.799506, 1.439605, 1.151684], 'p_i': 40, 'u_i': 3.8857},
        {'id': 5, 'e_m': 1.641297, 'e_o_k': [1.276564, 1.021251], 'p_i': 20, 'u_i': 4.4773},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET

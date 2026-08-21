"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.19999, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.19999, "H": 80, "J": 21, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.242482, 'e_o_k': [0.052585, 0.031551, 0.018931, 0.011358, 0.006815], 'p_i': 10, 'u_i': 1.7042},
        {'id': 1, 'e_m': 0.368320, 'e_o_k': [0.093959, 0.056376, 0.033825], 'p_i': 20, 'u_i': 4.3788},
        {'id': 2, 'e_m': 2.283808, 'e_o_k': [0.524772, 0.314863, 0.188918, 0.113351], 'p_i': 40, 'u_i': 3.2500},
        {'id': 3, 'e_m': 1.295241, 'e_o_k': [0.404763, 0.242858], 'p_i': 80, 'u_i': 3.9101},
        {'id': 4, 'e_m': 0.598180, 'e_o_k': [0.137449, 0.082470, 0.049482, 0.029689], 'p_i': 80, 'u_i': 2.7187},
        {'id': 5, 'e_m': 2.822117, 'e_o_k': [0.592046, 0.355228, 0.213137, 0.127882, 0.076729, 0.046037], 'p_i': 40, 'u_i': 3.8755},
        {'id': 6, 'e_m': 12.997943, 'e_o_k': [3.315802, 1.989481, 1.193689], 'p_i': 80, 'u_i': 3.4836},
        {'id': 7, 'e_m': 1.741824, 'e_o_k': [0.444343, 0.266606, 0.159963], 'p_i': 40, 'u_i': 4.1699},
    ]
    B_BUDGET = 55.199990
    return processors, tasks, B_BUDGET

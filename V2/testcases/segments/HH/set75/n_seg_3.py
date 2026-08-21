"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.893774, 'e_o_k': [0.512821, 0.410257, 0.328205], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.002051, 'e_o_k': [0.001177, 0.000941, 0.000753], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 13.125199, 'e_o_k': [7.530852, 6.024681, 4.819745], 'p_i': 40, 'u_i': 2.6491},
        {'id': 3, 'e_m': 4.683481, 'e_o_k': [2.687243, 2.149795, 1.719836], 'p_i': 80, 'u_i': 3.7785},
        {'id': 4, 'e_m': 0.355356, 'e_o_k': [0.203893, 0.163114, 0.130491], 'p_i': 10, 'u_i': 2.0110},
        {'id': 5, 'e_m': 0.683705, 'e_o_k': [0.392290, 0.313832, 0.251066], 'p_i': 10, 'u_i': 2.7392},
        {'id': 6, 'e_m': 12.075953, 'e_o_k': [6.928826, 5.543061, 4.434448], 'p_i': 80, 'u_i': 4.5700},
        {'id': 7, 'e_m': 1.379822, 'e_o_k': [0.791701, 0.633361, 0.506689], 'p_i': 20, 'u_i': 2.3393},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET

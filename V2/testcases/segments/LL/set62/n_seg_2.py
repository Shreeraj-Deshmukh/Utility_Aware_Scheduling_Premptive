"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199994, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199994, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.059251, 'e_o_k': [0.294236, 0.235389], 'p_i': 10, 'u_i': 2.6711},
        {'id': 1, 'e_m': 0.937251, 'e_o_k': [0.260347, 0.208278], 'p_i': 20, 'u_i': 2.3833},
        {'id': 2, 'e_m': 0.643315, 'e_o_k': [0.178699, 0.142959], 'p_i': 40, 'u_i': 4.1647},
        {'id': 3, 'e_m': 0.856471, 'e_o_k': [0.237909, 0.190327], 'p_i': 80, 'u_i': 1.2796},
        {'id': 4, 'e_m': 1.453835, 'e_o_k': [0.403843, 0.323074], 'p_i': 10, 'u_i': 2.4526},
        {'id': 5, 'e_m': 0.242032, 'e_o_k': [0.067231, 0.053785], 'p_i': 10, 'u_i': 3.7482},
        {'id': 6, 'e_m': 3.782251, 'e_o_k': [1.050625, 0.840500], 'p_i': 80, 'u_i': 2.1247},
        {'id': 7, 'e_m': 0.142351, 'e_o_k': [0.039542, 0.031634], 'p_i': 40, 'u_i': 4.6336},
    ]
    B_BUDGET = 55.199994
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200011, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200011, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.059251, 'e_o_k': [0.217060, 0.173648, 0.138918], 'p_i': 10, 'u_i': 2.6711},
        {'id': 1, 'e_m': 0.937251, 'e_o_k': [0.192060, 0.153648, 0.122918], 'p_i': 20, 'u_i': 2.3833},
        {'id': 2, 'e_m': 0.643315, 'e_o_k': [0.131827, 0.105461, 0.084369], 'p_i': 40, 'u_i': 4.1647},
        {'id': 3, 'e_m': 0.856471, 'e_o_k': [0.175506, 0.140405, 0.112324], 'p_i': 80, 'u_i': 1.2796},
        {'id': 4, 'e_m': 1.453835, 'e_o_k': [0.297917, 0.238334, 0.190667], 'p_i': 10, 'u_i': 2.4526},
        {'id': 5, 'e_m': 0.242032, 'e_o_k': [0.049597, 0.039677, 0.031742], 'p_i': 10, 'u_i': 3.7482},
        {'id': 6, 'e_m': 3.782251, 'e_o_k': [0.775051, 0.620041, 0.496033], 'p_i': 80, 'u_i': 2.1247},
        {'id': 7, 'e_m': 0.142351, 'e_o_k': [0.029170, 0.023336, 0.018669], 'p_i': 40, 'u_i': 4.6336},
    ]
    B_BUDGET = 55.200011
    return processors, tasks, B_BUDGET

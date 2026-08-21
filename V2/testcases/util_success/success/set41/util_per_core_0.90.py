"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279983, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279983, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.813321, 'e_o_k': [0.161827, 0.129461, 0.103569, 0.082855, 0.066284], 'p_i': 10, 'u_i': 1.5284},
        {'id': 1, 'e_m': 1.020983, 'e_o_k': [0.103758, 0.083007, 0.066405, 0.053124], 'p_i': 20, 'u_i': 4.7182},
        {'id': 2, 'e_m': 4.823711, 'e_o_k': [0.490215, 0.392172, 0.313737, 0.250990], 'p_i': 40, 'u_i': 3.4247},
        {'id': 3, 'e_m': 23.599750, 'e_o_k': [2.398349, 1.918679, 1.534943, 1.227954], 'p_i': 80, 'u_i': 4.7267},
        {'id': 4, 'e_m': 39.885037, 'e_o_k': [4.053357, 3.242686, 2.594149, 2.075319], 'p_i': 80, 'u_i': 3.5037},
        {'id': 5, 'e_m': 0.181756, 'e_o_k': [0.016221, 0.012976, 0.010381, 0.008305, 0.006644], 'p_i': 10, 'u_i': 1.8182},
        {'id': 6, 'e_m': 17.743881, 'e_o_k': [1.803240, 1.442592, 1.154074, 0.923259], 'p_i': 40, 'u_i': 2.8197},
        {'id': 7, 'e_m': 1.916934, 'e_o_k': [0.194810, 0.155848, 0.124679, 0.099743], 'p_i': 10, 'u_i': 3.0802},
    ]
    B_BUDGET = 215.279983
    return processors, tasks, B_BUDGET

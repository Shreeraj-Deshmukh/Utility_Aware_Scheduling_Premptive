"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360018, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360018, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.720373, 'e_o_k': [0.064288, 0.051431, 0.041145, 0.032916, 0.026333], 'p_i': 10, 'u_i': 2.4242},
        {'id': 1, 'e_m': 6.332255, 'e_o_k': [0.565111, 0.452089, 0.361671, 0.289337, 0.231469], 'p_i': 20, 'u_i': 1.3497},
        {'id': 2, 'e_m': 1.156384, 'e_o_k': [0.117519, 0.094015, 0.075212, 0.060170], 'p_i': 40, 'u_i': 4.8973},
        {'id': 3, 'e_m': 20.851757, 'e_o_k': [1.695596, 1.356476, 1.085181, 0.868145, 0.694516, 0.555613], 'p_i': 80, 'u_i': 4.4724},
        {'id': 4, 'e_m': 5.681600, 'e_o_k': [0.698557, 0.558846, 0.447077], 'p_i': 20, 'u_i': 4.7464},
        {'id': 5, 'e_m': 0.757743, 'e_o_k': [0.093165, 0.074532, 0.059626], 'p_i': 10, 'u_i': 2.8305},
        {'id': 6, 'e_m': 16.958510, 'e_o_k': [2.826418, 2.261135], 'p_i': 40, 'u_i': 4.0659},
        {'id': 7, 'e_m': 11.038109, 'e_o_k': [0.897582, 0.718066, 0.574453, 0.459562, 0.367650, 0.294120], 'p_i': 80, 'u_i': 3.0796},
    ]
    B_BUDGET = 191.360018
    return processors, tasks, B_BUDGET

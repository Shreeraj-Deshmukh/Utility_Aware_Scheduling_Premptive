"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.27999, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.27999, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.573684, 'e_o_k': [0.595614, 0.476491], 'p_i': 10, 'u_i': 1.1590},
        {'id': 1, 'e_m': 9.357201, 'e_o_k': [1.559534, 1.247627], 'p_i': 20, 'u_i': 4.3960},
        {'id': 2, 'e_m': 11.357904, 'e_o_k': [1.013616, 0.810893, 0.648714, 0.518971, 0.415177], 'p_i': 40, 'u_i': 2.4870},
        {'id': 3, 'e_m': 9.797377, 'e_o_k': [0.796690, 0.637352, 0.509882, 0.407905, 0.326324, 0.261059], 'p_i': 80, 'u_i': 2.1849},
        {'id': 4, 'e_m': 9.109077, 'e_o_k': [0.812923, 0.650339, 0.520271, 0.416217, 0.332973], 'p_i': 40, 'u_i': 2.3820},
        {'id': 5, 'e_m': 1.893464, 'e_o_k': [0.168979, 0.135183, 0.108146, 0.086517, 0.069214], 'p_i': 40, 'u_i': 1.7984},
        {'id': 6, 'e_m': 11.333621, 'e_o_k': [1.393478, 1.114782, 0.891826], 'p_i': 40, 'u_i': 4.6658},
        {'id': 7, 'e_m': 0.398105, 'e_o_k': [0.048947, 0.039158, 0.031326], 'p_i': 40, 'u_i': 1.0345},
    ]
    B_BUDGET = 215.279990
    return processors, tasks, B_BUDGET

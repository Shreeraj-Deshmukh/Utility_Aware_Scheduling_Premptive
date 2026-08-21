"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.67999, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.67999, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.147016, 'e_o_k': [0.191169, 0.152936], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 3.773755, 'e_o_k': [0.628959, 0.503167], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 5.350477, 'e_o_k': [0.657846, 0.526276, 0.421021], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 16.969247, 'e_o_k': [1.514390, 1.211512, 0.969210, 0.775368, 0.620294], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 1.099497, 'e_o_k': [0.135184, 0.108147, 0.086518], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.148964, 'e_o_k': [0.013294, 0.010635, 0.008508, 0.006807, 0.005445], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 3.297912, 'e_o_k': [0.268175, 0.214540, 0.171632, 0.137306, 0.109845, 0.087876], 'p_i': 80, 'u_i': 4.6383},
        {'id': 7, 'e_m': 3.766890, 'e_o_k': [0.336169, 0.268935, 0.215148, 0.172119, 0.137695], 'p_i': 80, 'u_i': 3.5515},
    ]
    B_BUDGET = 95.679990
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.689807, 'e_o_k': [1.026080, 0.615648, 0.369389, 0.221633, 0.132980], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.355169, 'e_o_k': [0.310773, 0.186464], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 2.867086, 'e_o_k': [1.844633, 1.106780, 0.664068, 0.398441], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 3.497724, 'e_o_k': [3.060509, 1.836305], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 13.830064, 'e_o_k': [8.123863, 4.874318, 2.924591, 1.754754, 1.052853, 0.631712], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 3.101531, 'e_o_k': [1.995470, 1.197282, 0.718369, 0.431022], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.222281, 'e_o_k': [0.194496, 0.116698], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 2.953634, 'e_o_k': [1.734982, 1.040989, 0.624594, 0.374756, 0.224854, 0.134912], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET

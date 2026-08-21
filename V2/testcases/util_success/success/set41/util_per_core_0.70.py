"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.439985, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.439985, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.410361, 'e_o_k': [0.125865, 0.100692, 0.080554, 0.064443, 0.051554], 'p_i': 10, 'u_i': 1.5284},
        {'id': 1, 'e_m': 0.794098, 'e_o_k': [0.080701, 0.064561, 0.051649, 0.041319], 'p_i': 20, 'u_i': 4.7182},
        {'id': 2, 'e_m': 3.751775, 'e_o_k': [0.381278, 0.305022, 0.244018, 0.195214], 'p_i': 40, 'u_i': 3.4247},
        {'id': 3, 'e_m': 18.355361, 'e_o_k': [1.865382, 1.492306, 1.193845, 0.955076], 'p_i': 80, 'u_i': 4.7267},
        {'id': 4, 'e_m': 31.021695, 'e_o_k': [3.152611, 2.522089, 2.017671, 1.614137], 'p_i': 80, 'u_i': 3.5037},
        {'id': 5, 'e_m': 0.141366, 'e_o_k': [0.012616, 0.010093, 0.008074, 0.006459, 0.005167], 'p_i': 10, 'u_i': 1.8182},
        {'id': 6, 'e_m': 13.800797, 'e_o_k': [1.402520, 1.122016, 0.897613, 0.718090], 'p_i': 40, 'u_i': 2.8197},
        {'id': 7, 'e_m': 1.490949, 'e_o_k': [0.151519, 0.121215, 0.096972, 0.077578], 'p_i': 10, 'u_i': 3.0802},
    ]
    B_BUDGET = 167.439985
    return processors, tasks, B_BUDGET

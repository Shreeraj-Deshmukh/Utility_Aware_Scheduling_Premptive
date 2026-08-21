"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520014, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520014, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.572390, 'e_o_k': [0.595398, 0.476319], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 1.077427, 'e_o_k': [0.109495, 0.087596, 0.070077, 0.056061], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 2.495560, 'e_o_k': [0.222712, 0.178169, 0.142536, 0.114028, 0.091223], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 31.262280, 'e_o_k': [3.177061, 2.541649, 2.033319, 1.626655], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 1.971380, 'e_o_k': [0.328563, 0.262851], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 1.104160, 'e_o_k': [0.098539, 0.078831, 0.063065, 0.050452, 0.040361], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 1.902595, 'e_o_k': [0.233926, 0.187141, 0.149712], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 1.264299, 'e_o_k': [0.112830, 0.090264, 0.072211, 0.057769, 0.046215], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 143.520014
    return processors, tasks, B_BUDGET

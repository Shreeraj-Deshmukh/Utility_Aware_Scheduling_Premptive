"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520003, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520003, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.158730, 'e_o_k': [0.265418, 0.212334, 0.169867], 'p_i': 10, 'u_i': 3.9504},
        {'id': 1, 'e_m': 3.119040, 'e_o_k': [0.278353, 0.222683, 0.178146, 0.142517, 0.114013], 'p_i': 20, 'u_i': 2.1226},
        {'id': 2, 'e_m': 0.441490, 'e_o_k': [0.073582, 0.058865], 'p_i': 40, 'u_i': 2.4300},
        {'id': 3, 'e_m': 1.972553, 'e_o_k': [0.176037, 0.140830, 0.112664, 0.090131, 0.072105], 'p_i': 80, 'u_i': 4.3958},
        {'id': 4, 'e_m': 13.440677, 'e_o_k': [1.092951, 0.874361, 0.699489, 0.559591, 0.447673, 0.358138], 'p_i': 80, 'u_i': 4.7703},
        {'id': 5, 'e_m': 0.073373, 'e_o_k': [0.005966, 0.004773, 0.003819, 0.003055, 0.002444, 0.001955], 'p_i': 80, 'u_i': 1.8568},
        {'id': 6, 'e_m': 3.001373, 'e_o_k': [0.369021, 0.295217, 0.236174], 'p_i': 20, 'u_i': 1.8128},
        {'id': 7, 'e_m': 18.939463, 'e_o_k': [3.156577, 2.525262], 'p_i': 40, 'u_i': 1.5689},
    ]
    B_BUDGET = 143.520003
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.126957, 'e_o_k': [0.098744, 0.078996], 'p_i': 10, 'u_i': 1.1447},
        {'id': 1, 'e_m': 1.222248, 'e_o_k': [0.950638, 0.760510], 'p_i': 20, 'u_i': 4.1970},
        {'id': 2, 'e_m': 0.719201, 'e_o_k': [0.559378, 0.447503], 'p_i': 40, 'u_i': 2.1490},
        {'id': 3, 'e_m': 4.503453, 'e_o_k': [3.502686, 2.802148], 'p_i': 80, 'u_i': 1.5069},
        {'id': 4, 'e_m': 0.473711, 'e_o_k': [0.368442, 0.294754], 'p_i': 20, 'u_i': 3.9372},
        {'id': 5, 'e_m': 0.486550, 'e_o_k': [0.378428, 0.302742], 'p_i': 20, 'u_i': 1.6580},
        {'id': 6, 'e_m': 0.523150, 'e_o_k': [0.406894, 0.325515], 'p_i': 20, 'u_i': 4.1894},
        {'id': 7, 'e_m': 14.219851, 'e_o_k': [11.059884, 8.847907], 'p_i': 80, 'u_i': 4.9102},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET

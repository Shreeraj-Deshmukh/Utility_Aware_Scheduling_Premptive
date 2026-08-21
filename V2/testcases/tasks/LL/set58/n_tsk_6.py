"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.852681, 'e_o_k': [0.236856, 0.189485], 'p_i': 10, 'u_i': 1.4573},
        {'id': 1, 'e_m': 2.529372, 'e_o_k': [0.376215, 0.300972, 0.240778, 0.192622, 0.154098], 'p_i': 20, 'u_i': 1.2598},
        {'id': 2, 'e_m': 0.360578, 'e_o_k': [0.048868, 0.039095, 0.031276, 0.025021, 0.020016, 0.016013], 'p_i': 40, 'u_i': 4.1820},
        {'id': 3, 'e_m': 3.676304, 'e_o_k': [1.021196, 0.816957], 'p_i': 80, 'u_i': 2.8729},
        {'id': 4, 'e_m': 1.338365, 'e_o_k': [0.274255, 0.219404, 0.175523], 'p_i': 20, 'u_i': 4.4646},
        {'id': 5, 'e_m': 0.663768, 'e_o_k': [0.184380, 0.147504], 'p_i': 10, 'u_i': 2.8456},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET

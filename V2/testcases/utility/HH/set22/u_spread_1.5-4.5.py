"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 30, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 30, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "utility", "util_per_core": 0.4, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.006839, 'e_o_k': [0.951753, 0.761402, 0.609122, 0.487298], 'p_i': 10, 'u_i': 2.9497},
        {'id': 1, 'e_m': 0.143860, 'e_o_k': [0.068226, 0.054581, 0.043665, 0.034932], 'p_i': 20, 'u_i': 4.0162},
        {'id': 2, 'e_m': 4.365284, 'e_o_k': [1.818002, 1.454402, 1.163522, 0.930817, 0.744654], 'p_i': 40, 'u_i': 2.4556},
        {'id': 3, 'e_m': 1.921148, 'e_o_k': [1.102298, 0.881838, 0.705471], 'p_i': 80, 'u_i': 2.6856},
        {'id': 4, 'e_m': 3.369376, 'e_o_k': [1.403238, 1.122591, 0.898073, 0.718458, 0.574766], 'p_i': 40, 'u_i': 4.1517},
        {'id': 5, 'e_m': 1.402420, 'e_o_k': [0.804667, 0.643734, 0.514987], 'p_i': 20, 'u_i': 4.0598},
        {'id': 6, 'e_m': 6.817126, 'e_o_k': [3.911466, 3.129173, 2.503338], 'p_i': 80, 'u_i': 1.5979},
        {'id': 7, 'e_m': 2.194072, 'e_o_k': [1.040549, 0.832439, 0.665951, 0.532761], 'p_i': 10, 'u_i': 4.3280},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET

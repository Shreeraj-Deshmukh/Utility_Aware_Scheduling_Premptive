"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280014, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280014, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.832931, 'e_o_k': [0.230365, 0.184292, 0.147433, 0.117947, 0.094357, 0.075486], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 8.798967, 'e_o_k': [1.466495, 1.173196], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 1.249502, 'e_o_k': [0.153627, 0.122902, 0.098322], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 11.514063, 'e_o_k': [1.919010, 1.535208], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 1.869688, 'e_o_k': [0.190009, 0.152007, 0.121606, 0.097285], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 31.494339, 'e_o_k': [5.249057, 4.199245], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 2.985943, 'e_o_k': [0.303449, 0.242760, 0.194208, 0.155366], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.223529, 'e_o_k': [0.022716, 0.018173, 0.014538, 0.011631], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 215.280014
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519998, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519998, "H": 80, "J": 40, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.888621, 'e_o_k': [0.153576, 0.122861, 0.098289, 0.078631, 0.062905, 0.050324], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 5.865978, 'e_o_k': [0.977663, 0.782130], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.833002, 'e_o_k': [0.102418, 0.081935, 0.065548], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 7.676042, 'e_o_k': [1.279340, 1.023472], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 1.246459, 'e_o_k': [0.126673, 0.101338, 0.081070, 0.064856], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 20.996226, 'e_o_k': [3.499371, 2.799497], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 1.990629, 'e_o_k': [0.202300, 0.161840, 0.129472, 0.103577], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.149019, 'e_o_k': [0.015144, 0.012115, 0.009692, 0.007754], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 143.519998
    return processors, tasks, B_BUDGET

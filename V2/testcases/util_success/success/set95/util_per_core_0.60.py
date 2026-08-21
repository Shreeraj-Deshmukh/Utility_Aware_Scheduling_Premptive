"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519995, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.375733, 'e_o_k': [0.241436, 0.193149, 0.154519, 0.123615], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 4.365281, 'e_o_k': [0.727547, 0.582037], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 10.234847, 'e_o_k': [0.832264, 0.665811, 0.532649, 0.426119, 0.340895, 0.272716], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 4.529506, 'e_o_k': [0.556907, 0.445525, 0.356420], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 5.874616, 'e_o_k': [0.477704, 0.382163, 0.305731, 0.244585, 0.195668, 0.156534], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 4.059699, 'e_o_k': [0.499143, 0.399315, 0.319452], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 12.346942, 'e_o_k': [1.101881, 0.881505, 0.705204, 0.564163, 0.451330], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 2.048214, 'e_o_k': [0.208152, 0.166522, 0.133217, 0.106574], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 143.519995
    return processors, tasks, B_BUDGET

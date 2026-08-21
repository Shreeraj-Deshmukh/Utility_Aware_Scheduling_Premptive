"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 73.600002, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.0, "seed": 1006, "set": 6, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.00"}
"""

_SPEC = '{"B": 73.600002, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.0, "seed": 1006, "set": 6, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.123701, 'e_o_k': [0.873989, 0.699191], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 2.998422, 'e_o_k': [1.422016, 1.137613, 0.910090, 0.728072], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 12.570386, 'e_o_k': [5.961565, 4.769252, 3.815402, 3.052321], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.317492, 'e_o_k': [0.246938, 0.197550], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 2.758630, 'e_o_k': [1.308294, 1.046635, 0.837308, 0.669846], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 2.930909, 'e_o_k': [2.279596, 1.823677], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.031369, 'e_o_k': [0.013064, 0.010451, 0.008361, 0.006689, 0.005351], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.066594, 'e_o_k': [0.027734, 0.022188, 0.017750, 0.014200, 0.011360], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 73.600002
    return processors, tasks, B_BUDGET

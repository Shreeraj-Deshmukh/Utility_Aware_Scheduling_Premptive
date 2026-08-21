"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.19999, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.19999, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.728605, 'e_o_k': [0.212533, 0.170027, 0.136021], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 9.127943, 'e_o_k': [0.742254, 0.593803, 0.475043, 0.380034, 0.304027, 0.243222], 'p_i': 20, 'u_i': 1.0830},
        {'id': 2, 'e_m': 13.424274, 'e_o_k': [2.237379, 1.789903], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 24.134252, 'e_o_k': [1.962517, 1.570014, 1.256011, 1.004809, 0.803847, 0.643078], 'p_i': 80, 'u_i': 2.8864},
        {'id': 4, 'e_m': 1.892031, 'e_o_k': [0.168851, 0.135081, 0.108065, 0.086452, 0.069161], 'p_i': 10, 'u_i': 1.3892},
        {'id': 5, 'e_m': 1.874101, 'e_o_k': [0.190457, 0.152366, 0.121893, 0.097514], 'p_i': 10, 'u_i': 2.4866},
        {'id': 6, 'e_m': 16.871565, 'e_o_k': [1.505673, 1.204538, 0.963631, 0.770904, 0.616724], 'p_i': 80, 'u_i': 4.5153},
        {'id': 7, 'e_m': 5.837980, 'e_o_k': [0.521000, 0.416800, 0.333440, 0.266752, 0.213402], 'p_i': 40, 'u_i': 1.1207},
    ]
    B_BUDGET = 239.199990
    return processors, tasks, B_BUDGET

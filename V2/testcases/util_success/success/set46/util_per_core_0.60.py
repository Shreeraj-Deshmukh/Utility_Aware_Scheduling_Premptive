"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.256268, 'e_o_k': [0.154459, 0.123567, 0.098854], 'p_i': 10, 'u_i': 3.9687},
        {'id': 1, 'e_m': 0.750370, 'e_o_k': [0.061018, 0.048814, 0.039051, 0.031241, 0.024993, 0.019994], 'p_i': 20, 'u_i': 2.3030},
        {'id': 2, 'e_m': 15.917042, 'e_o_k': [1.957013, 1.565611, 1.252489], 'p_i': 40, 'u_i': 2.6501},
        {'id': 3, 'e_m': 11.411951, 'e_o_k': [1.018439, 0.814751, 0.651801, 0.521441, 0.417153], 'p_i': 80, 'u_i': 1.7748},
        {'id': 4, 'e_m': 4.239271, 'e_o_k': [0.521222, 0.416977, 0.333582], 'p_i': 20, 'u_i': 3.9815},
        {'id': 5, 'e_m': 0.193580, 'e_o_k': [0.015741, 0.012593, 0.010074, 0.008060, 0.006448, 0.005158], 'p_i': 10, 'u_i': 4.8257},
        {'id': 6, 'e_m': 1.782283, 'e_o_k': [0.159057, 0.127245, 0.101796, 0.081437, 0.065150], 'p_i': 40, 'u_i': 1.0600},
        {'id': 7, 'e_m': 8.816027, 'e_o_k': [0.786771, 0.629416, 0.503533, 0.402827, 0.322261], 'p_i': 40, 'u_i': 2.2764},
    ]
    B_BUDGET = 143.520000
    return processors, tasks, B_BUDGET

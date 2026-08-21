"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 24, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.622255, 'e_o_k': [1.508555, 1.206844, 0.965475, 0.772380, 0.617904], 'p_i': 10, 'u_i': 3.1078},
        {'id': 1, 'e_m': 0.101434, 'e_o_k': [0.048105, 0.038484, 0.030787, 0.024630], 'p_i': 20, 'u_i': 3.2194},
        {'id': 2, 'e_m': 5.088426, 'e_o_k': [3.957665, 3.166132], 'p_i': 40, 'u_i': 3.0805},
        {'id': 3, 'e_m': 2.359092, 'e_o_k': [1.834849, 1.467879], 'p_i': 80, 'u_i': 2.8827},
        {'id': 4, 'e_m': 3.488235, 'e_o_k': [2.001446, 1.601157, 1.280925], 'p_i': 40, 'u_i': 3.1782},
        {'id': 5, 'e_m': 1.158934, 'e_o_k': [0.901393, 0.721114], 'p_i': 20, 'u_i': 3.4893},
        {'id': 6, 'e_m': 9.098933, 'e_o_k': [5.220699, 4.176559, 3.341248], 'p_i': 80, 'u_i': 3.2333},
        {'id': 7, 'e_m': 0.684572, 'e_o_k': [0.392787, 0.314230, 0.251384], 'p_i': 40, 'u_i': 3.1471},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET

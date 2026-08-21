"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199993, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199993, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.569386, 'e_o_k': [0.261564, 0.209252], 'p_i': 10, 'u_i': 2.5239},
        {'id': 1, 'e_m': 6.086276, 'e_o_k': [1.014379, 0.811504], 'p_i': 20, 'u_i': 1.8339},
        {'id': 2, 'e_m': 7.695041, 'e_o_k': [0.782016, 0.625613, 0.500490, 0.400392], 'p_i': 40, 'u_i': 4.8055},
        {'id': 3, 'e_m': 32.321484, 'e_o_k': [5.386914, 4.309531], 'p_i': 80, 'u_i': 3.2084},
        {'id': 4, 'e_m': 3.012586, 'e_o_k': [0.370400, 0.296320, 0.237056], 'p_i': 20, 'u_i': 1.8854},
        {'id': 5, 'e_m': 3.688522, 'e_o_k': [0.299938, 0.239951, 0.191961, 0.153568, 0.122855, 0.098284], 'p_i': 10, 'u_i': 4.9503},
        {'id': 6, 'e_m': 19.153868, 'e_o_k': [1.709353, 1.367482, 1.093986, 0.875189, 0.700151], 'p_i': 80, 'u_i': 3.0972},
        {'id': 7, 'e_m': 14.675846, 'e_o_k': [1.804407, 1.443526, 1.154821], 'p_i': 80, 'u_i': 2.5144},
    ]
    B_BUDGET = 239.199993
    return processors, tasks, B_BUDGET

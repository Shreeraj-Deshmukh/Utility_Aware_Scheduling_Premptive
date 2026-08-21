"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120002, "H": 80, "J": 26, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.727227, 'e_o_k': [0.212364, 0.169891, 0.135913], 'p_i': 10, 'u_i': 4.8356},
        {'id': 1, 'e_m': 2.351452, 'e_o_k': [0.238969, 0.191175, 0.152940, 0.122352], 'p_i': 20, 'u_i': 2.0758},
        {'id': 2, 'e_m': 18.727808, 'e_o_k': [2.302599, 1.842079, 1.473664], 'p_i': 40, 'u_i': 3.9792},
        {'id': 3, 'e_m': 25.244363, 'e_o_k': [3.103815, 2.483052, 1.986442], 'p_i': 80, 'u_i': 1.3854},
        {'id': 4, 'e_m': 0.671744, 'e_o_k': [0.068267, 0.054613, 0.043691, 0.034953], 'p_i': 40, 'u_i': 2.0294},
        {'id': 5, 'e_m': 37.780974, 'e_o_k': [4.645202, 3.716161, 2.972929], 'p_i': 80, 'u_i': 2.2362},
        {'id': 6, 'e_m': 8.273006, 'e_o_k': [0.672733, 0.538187, 0.430549, 0.344439, 0.275552, 0.220441], 'p_i': 20, 'u_i': 4.4908},
        {'id': 7, 'e_m': 4.464979, 'e_o_k': [0.744163, 0.595330], 'p_i': 20, 'u_i': 1.3350},
    ]
    B_BUDGET = 263.120002
    return processors, tasks, B_BUDGET

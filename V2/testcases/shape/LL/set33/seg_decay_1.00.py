"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200012, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200012, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.024096, 'e_o_k': [0.004016, 0.004016, 0.004016], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 1.824026, 'e_o_k': [0.304004, 0.304004, 0.304004], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 2.806108, 'e_o_k': [0.467685, 0.467685, 0.467685], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 0.481622, 'e_o_k': [0.120406, 0.120406], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 2.721725, 'e_o_k': [0.272173, 0.272173, 0.272173, 0.272173, 0.272173], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 0.681310, 'e_o_k': [0.068131, 0.068131, 0.068131, 0.068131, 0.068131], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 0.612959, 'e_o_k': [0.153240, 0.153240], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 1.466951, 'e_o_k': [0.183369, 0.183369, 0.183369, 0.183369], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 55.200012
    return processors, tasks, B_BUDGET

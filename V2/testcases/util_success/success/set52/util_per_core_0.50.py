"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600009, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600009, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.090542, 'e_o_k': [0.007363, 0.005890, 0.004712, 0.003770, 0.003016, 0.002413], 'p_i': 10, 'u_i': 2.1441},
        {'id': 1, 'e_m': 1.435210, 'e_o_k': [0.128083, 0.102466, 0.081973, 0.065578, 0.052463], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 12.612446, 'e_o_k': [1.281753, 1.025402, 0.820322, 0.656257], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 19.543059, 'e_o_k': [2.402835, 1.922268, 1.537815], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 6.634741, 'e_o_k': [1.105790, 0.884632], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 5.410454, 'e_o_k': [0.665220, 0.532176, 0.425741], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 5.829407, 'e_o_k': [0.592419, 0.473935, 0.379148, 0.303319], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 2.740907, 'e_o_k': [0.244607, 0.195686, 0.156549, 0.125239, 0.100191], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 119.600009
    return processors, tasks, B_BUDGET

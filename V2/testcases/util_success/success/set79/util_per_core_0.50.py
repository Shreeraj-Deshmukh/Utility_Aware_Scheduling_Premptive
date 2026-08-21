"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599994, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599994, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.850204, 'e_o_k': [0.075875, 0.060700, 0.048560, 0.038848, 0.031078], 'p_i': 10, 'u_i': 4.9110},
        {'id': 1, 'e_m': 2.112317, 'e_o_k': [0.171767, 0.137413, 0.109931, 0.087944, 0.070356, 0.056284], 'p_i': 20, 'u_i': 1.5555},
        {'id': 2, 'e_m': 0.649519, 'e_o_k': [0.079859, 0.063887, 0.051110], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 22.618077, 'e_o_k': [3.769679, 3.015744], 'p_i': 80, 'u_i': 3.1608},
        {'id': 4, 'e_m': 6.262242, 'e_o_k': [1.043707, 0.834966], 'p_i': 80, 'u_i': 1.3239},
        {'id': 5, 'e_m': 2.444914, 'e_o_k': [0.248467, 0.198773, 0.159019, 0.127215], 'p_i': 80, 'u_i': 4.3282},
        {'id': 6, 'e_m': 13.438140, 'e_o_k': [2.239690, 1.791752], 'p_i': 40, 'u_i': 3.0285},
        {'id': 7, 'e_m': 5.248546, 'e_o_k': [0.533389, 0.426711, 0.341369, 0.273095], 'p_i': 80, 'u_i': 4.7214},
    ]
    B_BUDGET = 119.599994
    return processors, tasks, B_BUDGET

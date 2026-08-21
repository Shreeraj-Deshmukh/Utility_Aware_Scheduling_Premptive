"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759998, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759998, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.419304, 'e_o_k': [0.037420, 0.029936, 0.023949, 0.019159, 0.015327], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 1.211236, 'e_o_k': [0.098494, 0.078795, 0.063036, 0.050429, 0.040343, 0.032274], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 4.768534, 'e_o_k': [0.586295, 0.469036, 0.375229], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 11.662796, 'e_o_k': [1.185243, 0.948195, 0.758556, 0.606845], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.002748, 'e_o_k': [0.000458, 0.000366], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 2.906470, 'e_o_k': [0.357353, 0.285882, 0.228706], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 0.541979, 'e_o_k': [0.055079, 0.044063, 0.035251, 0.028201], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 5.668237, 'e_o_k': [0.576040, 0.460832, 0.368666, 0.294933], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 71.759998
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759999, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1033, "set": 33, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.036145, 'e_o_k': [0.004444, 0.003555, 0.002844], 'p_i': 10, 'u_i': 4.1859},
        {'id': 1, 'e_m': 2.736038, 'e_o_k': [0.336398, 0.269119, 0.215295], 'p_i': 20, 'u_i': 1.3758},
        {'id': 2, 'e_m': 4.209162, 'e_o_k': [0.517520, 0.414016, 0.331213], 'p_i': 40, 'u_i': 3.6848},
        {'id': 3, 'e_m': 0.722433, 'e_o_k': [0.120406, 0.096324], 'p_i': 80, 'u_i': 1.6851},
        {'id': 4, 'e_m': 4.082588, 'e_o_k': [0.364343, 0.291475, 0.233180, 0.186544, 0.149235], 'p_i': 20, 'u_i': 1.3700},
        {'id': 5, 'e_m': 1.021964, 'e_o_k': [0.091203, 0.072963, 0.058370, 0.046696, 0.037357], 'p_i': 10, 'u_i': 3.3252},
        {'id': 6, 'e_m': 0.919439, 'e_o_k': [0.153240, 0.122592], 'p_i': 80, 'u_i': 4.3008},
        {'id': 7, 'e_m': 2.200427, 'e_o_k': [0.223621, 0.178896, 0.143117, 0.114494], 'p_i': 80, 'u_i': 2.2362},
    ]
    B_BUDGET = 71.759999
    return processors, tasks, B_BUDGET

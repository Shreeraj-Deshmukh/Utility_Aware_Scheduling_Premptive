"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359999, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.013678, 'e_o_k': [0.407894, 0.326315, 0.261052, 0.208842], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.287720, 'e_o_k': [0.029240, 0.023392, 0.018714, 0.014971], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 8.730567, 'e_o_k': [0.779144, 0.623315, 0.498652, 0.398922, 0.319137], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 3.842295, 'e_o_k': [0.472413, 0.377931, 0.302345], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 6.738751, 'e_o_k': [0.601388, 0.481110, 0.384888, 0.307911, 0.246328], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 2.804840, 'e_o_k': [0.344857, 0.275886, 0.220709], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 13.634253, 'e_o_k': [1.676343, 1.341074, 1.072859], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 4.388143, 'e_o_k': [0.445950, 0.356760, 0.285408, 0.228326], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 191.359999
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.844903, 'e_o_k': [0.513040, 0.307824, 0.184694, 0.110817, 0.066490], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.177585, 'e_o_k': [0.155387, 0.093232], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 1.433543, 'e_o_k': [0.922316, 0.553390, 0.332034, 0.199220], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 1.748862, 'e_o_k': [1.530254, 0.918153], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 6.915032, 'e_o_k': [4.061931, 2.437159, 1.462295, 0.877377, 0.526426, 0.315856], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 1.550765, 'e_o_k': [0.997735, 0.598641, 0.359185, 0.215511], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.111141, 'e_o_k': [0.097248, 0.058349], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 1.476817, 'e_o_k': [0.867491, 0.520495, 0.312297, 0.187378, 0.112427, 0.067456], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET

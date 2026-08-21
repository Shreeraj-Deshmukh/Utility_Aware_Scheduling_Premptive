"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359989, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359989, "H": 80, "J": 23, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.706883, 'e_o_k': [0.057481, 0.045985, 0.036788, 0.029430, 0.023544, 0.018836], 'p_i': 10, 'u_i': 1.3055},
        {'id': 1, 'e_m': 7.112724, 'e_o_k': [0.578383, 0.462706, 0.370165, 0.296132, 0.236906, 0.189525], 'p_i': 20, 'u_i': 3.0735},
        {'id': 2, 'e_m': 1.674258, 'e_o_k': [0.170148, 0.136119, 0.108895, 0.087116], 'p_i': 40, 'u_i': 3.9862},
        {'id': 3, 'e_m': 14.032317, 'e_o_k': [1.725285, 1.380228, 1.104182], 'p_i': 80, 'u_i': 1.5757},
        {'id': 4, 'e_m': 3.891694, 'e_o_k': [0.478487, 0.382790, 0.306232], 'p_i': 20, 'u_i': 4.9941},
        {'id': 5, 'e_m': 0.101170, 'e_o_k': [0.016862, 0.013489], 'p_i': 80, 'u_i': 1.7632},
        {'id': 6, 'e_m': 25.825700, 'e_o_k': [2.304769, 1.843815, 1.475052, 1.180042, 0.944033], 'p_i': 80, 'u_i': 1.4284},
        {'id': 7, 'e_m': 17.509778, 'e_o_k': [2.918296, 2.334637], 'p_i': 40, 'u_i': 4.8320},
    ]
    B_BUDGET = 191.359989
    return processors, tasks, B_BUDGET

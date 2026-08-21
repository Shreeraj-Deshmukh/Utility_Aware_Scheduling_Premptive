"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320011, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.320011, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.728311, 'e_o_k': [0.254909, 0.254909, 0.254909, 0.254909], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 3.236491, 'e_o_k': [1.510363, 1.510363, 1.510363], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 0.535015, 'e_o_k': [0.249674, 0.249674, 0.249674], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 4.750488, 'e_o_k': [1.108447, 1.108447, 1.108447, 1.108447, 1.108447, 1.108447], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.182718, 'e_o_k': [0.127902, 0.127902], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.092022, 'e_o_k': [0.042944, 0.042944, 0.042944], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 2.641333, 'e_o_k': [0.924467, 0.924467, 0.924467, 0.924467], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.127844, 'e_o_k': [0.044745, 0.044745, 0.044745, 0.044745], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 88.320011
    return processors, tasks, B_BUDGET

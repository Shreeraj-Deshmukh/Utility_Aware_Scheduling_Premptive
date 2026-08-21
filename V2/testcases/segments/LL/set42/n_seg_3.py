"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.719577, 'e_o_k': [0.147454, 0.117963, 0.094371], 'p_i': 10, 'u_i': 3.9504},
        {'id': 1, 'e_m': 1.039680, 'e_o_k': [0.213049, 0.170439, 0.136351], 'p_i': 20, 'u_i': 2.1226},
        {'id': 2, 'e_m': 0.147163, 'e_o_k': [0.030156, 0.024125, 0.019300], 'p_i': 40, 'u_i': 2.4300},
        {'id': 3, 'e_m': 0.657518, 'e_o_k': [0.134737, 0.107790, 0.086232], 'p_i': 80, 'u_i': 4.3958},
        {'id': 4, 'e_m': 4.480226, 'e_o_k': [0.918079, 0.734463, 0.587571], 'p_i': 80, 'u_i': 3.0676},
        {'id': 5, 'e_m': 0.024458, 'e_o_k': [0.005012, 0.004009, 0.003208], 'p_i': 80, 'u_i': 1.8128},
        {'id': 6, 'e_m': 1.000458, 'e_o_k': [0.205012, 0.164009, 0.131208], 'p_i': 20, 'u_i': 1.5689},
        {'id': 7, 'e_m': 6.313154, 'e_o_k': [1.293679, 1.034943, 0.827955], 'p_i': 40, 'u_i': 4.8976},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET

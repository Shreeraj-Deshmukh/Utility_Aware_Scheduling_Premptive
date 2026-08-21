"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199992, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199992, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.728311, 'e_o_k': [0.149244, 0.119395, 0.095516], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 3.236491, 'e_o_k': [0.663215, 0.530572, 0.424458], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 0.535015, 'e_o_k': [0.109634, 0.087707, 0.070166], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 4.750488, 'e_o_k': [0.973461, 0.778769, 0.623015], 'p_i': 80, 'u_i': 4.1202},
        {'id': 4, 'e_m': 0.182718, 'e_o_k': [0.037442, 0.029954, 0.023963], 'p_i': 40, 'u_i': 4.7898},
        {'id': 5, 'e_m': 0.092022, 'e_o_k': [0.018857, 0.015086, 0.012068], 'p_i': 10, 'u_i': 3.8151},
        {'id': 6, 'e_m': 2.641333, 'e_o_k': [0.541257, 0.433005, 0.346404], 'p_i': 40, 'u_i': 2.4922},
        {'id': 7, 'e_m': 0.127844, 'e_o_k': [0.026198, 0.020958, 0.016766], 'p_i': 10, 'u_i': 1.4417},
    ]
    B_BUDGET = 55.199992
    return processors, tasks, B_BUDGET

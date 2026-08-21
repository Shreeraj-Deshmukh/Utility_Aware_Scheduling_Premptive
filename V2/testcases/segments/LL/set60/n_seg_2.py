"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.728311, 'e_o_k': [0.202309, 0.161847], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 3.236491, 'e_o_k': [0.899025, 0.719220], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 0.535015, 'e_o_k': [0.148615, 0.118892], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 4.750488, 'e_o_k': [1.319580, 1.055664], 'p_i': 80, 'u_i': 4.1202},
        {'id': 4, 'e_m': 0.182718, 'e_o_k': [0.050755, 0.040604], 'p_i': 40, 'u_i': 4.7898},
        {'id': 5, 'e_m': 0.092022, 'e_o_k': [0.025562, 0.020449], 'p_i': 10, 'u_i': 3.8151},
        {'id': 6, 'e_m': 2.641333, 'e_o_k': [0.733704, 0.586963], 'p_i': 40, 'u_i': 2.4922},
        {'id': 7, 'e_m': 0.127844, 'e_o_k': [0.035512, 0.028410], 'p_i': 10, 'u_i': 1.4417},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET

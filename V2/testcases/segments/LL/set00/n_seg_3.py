"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199997, "H": 80, "J": 29, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.141359, 'e_o_k': [0.028967, 0.023174, 0.018539], 'p_i': 10, 'u_i': 4.9222},
        {'id': 1, 'e_m': 0.498599, 'e_o_k': [0.102172, 0.081737, 0.065390], 'p_i': 20, 'u_i': 1.9107},
        {'id': 2, 'e_m': 5.343733, 'e_o_k': [1.095027, 0.876022, 0.700817], 'p_i': 40, 'u_i': 1.7322},
        {'id': 3, 'e_m': 4.168750, 'e_o_k': [0.854252, 0.683402, 0.546721], 'p_i': 80, 'u_i': 1.5709},
        {'id': 4, 'e_m': 0.783836, 'e_o_k': [0.160622, 0.128498, 0.102798], 'p_i': 20, 'u_i': 3.7661},
        {'id': 5, 'e_m': 0.731293, 'e_o_k': [0.149855, 0.119884, 0.095907], 'p_i': 20, 'u_i': 1.0932},
        {'id': 6, 'e_m': 0.043154, 'e_o_k': [0.008843, 0.007074, 0.005660], 'p_i': 20, 'u_i': 3.8665},
        {'id': 7, 'e_m': 3.892691, 'e_o_k': [0.797683, 0.638146, 0.510517], 'p_i': 40, 'u_i': 4.9324},
    ]
    B_BUDGET = 55.199997
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.822029, 'e_o_k': [0.168448, 0.134759, 0.107807], 'p_i': 10, 'u_i': 2.9699},
        {'id': 1, 'e_m': 0.158606, 'e_o_k': [0.032501, 0.026001, 0.020801], 'p_i': 20, 'u_i': 1.6736},
        {'id': 2, 'e_m': 0.584707, 'e_o_k': [0.119817, 0.095854, 0.076683], 'p_i': 40, 'u_i': 2.6796},
        {'id': 3, 'e_m': 6.151953, 'e_o_k': [1.260646, 1.008517, 0.806813], 'p_i': 80, 'u_i': 2.5270},
        {'id': 4, 'e_m': 1.208847, 'e_o_k': [0.247715, 0.198172, 0.158537], 'p_i': 20, 'u_i': 1.9244},
        {'id': 5, 'e_m': 0.880892, 'e_o_k': [0.180511, 0.144408, 0.115527], 'p_i': 10, 'u_i': 4.2011},
        {'id': 6, 'e_m': 0.518381, 'e_o_k': [0.106226, 0.084981, 0.067984], 'p_i': 40, 'u_i': 3.3831},
        {'id': 7, 'e_m': 1.137173, 'e_o_k': [0.233027, 0.186422, 0.149137], 'p_i': 20, 'u_i': 4.9669},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET

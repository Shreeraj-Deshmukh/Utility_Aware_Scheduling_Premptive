"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.498376, 'e_o_k': [0.138438, 0.110750], 'p_i': 10, 'u_i': 4.1058},
        {'id': 1, 'e_m': 0.297010, 'e_o_k': [0.082503, 0.066002], 'p_i': 20, 'u_i': 1.5782},
        {'id': 2, 'e_m': 0.891273, 'e_o_k': [0.247576, 0.198061], 'p_i': 40, 'u_i': 1.2072},
        {'id': 3, 'e_m': 2.329510, 'e_o_k': [0.647086, 0.517669], 'p_i': 80, 'u_i': 4.8515},
        {'id': 4, 'e_m': 0.437113, 'e_o_k': [0.121420, 0.097136], 'p_i': 20, 'u_i': 2.4561},
        {'id': 5, 'e_m': 9.162615, 'e_o_k': [2.545171, 2.036137], 'p_i': 80, 'u_i': 1.8035},
        {'id': 6, 'e_m': 0.776607, 'e_o_k': [0.215724, 0.172579], 'p_i': 20, 'u_i': 3.4846},
        {'id': 7, 'e_m': 1.086925, 'e_o_k': [0.301924, 0.241539], 'p_i': 10, 'u_i': 2.9402},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET

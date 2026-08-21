"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.799720, 'e_o_k': [0.622004, 0.497604], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 2.592762, 'e_o_k': [2.016592, 1.613274], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 1.461112, 'e_o_k': [1.136421, 0.909136], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 3.792245, 'e_o_k': [2.949524, 2.359619], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 0.519494, 'e_o_k': [0.404051, 0.323240], 'p_i': 40, 'u_i': 3.3706},
        {'id': 5, 'e_m': 0.710845, 'e_o_k': [0.552880, 0.442304], 'p_i': 20, 'u_i': 1.2465},
        {'id': 6, 'e_m': 1.584893, 'e_o_k': [1.232695, 0.986156], 'p_i': 40, 'u_i': 3.7304},
        {'id': 7, 'e_m': 0.183071, 'e_o_k': [0.142389, 0.113911], 'p_i': 10, 'u_i': 3.6440},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199987, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199987, "H": 80, "J": 40, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.629540, 'e_o_k': [0.174872, 0.139898], 'p_i': 10, 'u_i': 2.8729},
        {'id': 1, 'e_m': 1.955326, 'e_o_k': [0.543146, 0.434517], 'p_i': 20, 'u_i': 4.4646},
        {'id': 2, 'e_m': 0.277667, 'e_o_k': [0.077130, 0.061704], 'p_i': 40, 'u_i': 2.8456},
        {'id': 3, 'e_m': 2.558681, 'e_o_k': [0.710745, 0.568596], 'p_i': 80, 'u_i': 4.6357},
        {'id': 4, 'e_m': 0.415486, 'e_o_k': [0.115413, 0.092330], 'p_i': 10, 'u_i': 3.1275},
        {'id': 5, 'e_m': 6.998742, 'e_o_k': [1.944095, 1.555276], 'p_i': 80, 'u_i': 2.7677},
        {'id': 6, 'e_m': 0.663543, 'e_o_k': [0.184317, 0.147454], 'p_i': 10, 'u_i': 2.2237},
        {'id': 7, 'e_m': 0.049673, 'e_o_k': [0.013798, 0.011038], 'p_i': 10, 'u_i': 3.7702},
    ]
    B_BUDGET = 55.199987
    return processors, tasks, B_BUDGET

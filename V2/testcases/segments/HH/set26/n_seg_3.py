"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640008, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640008, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.261458, 'e_o_k': [1.871328, 1.497063, 1.197650], 'p_i': 10, 'u_i': 2.1780},
        {'id': 1, 'e_m': 1.108892, 'e_o_k': [0.636250, 0.509000, 0.407200], 'p_i': 20, 'u_i': 3.8388},
        {'id': 2, 'e_m': 2.887856, 'e_o_k': [1.656967, 1.325573, 1.060459], 'p_i': 40, 'u_i': 1.0041},
        {'id': 3, 'e_m': 7.831935, 'e_o_k': [4.493733, 3.594987, 2.875989], 'p_i': 80, 'u_i': 4.1994},
        {'id': 4, 'e_m': 1.667341, 'e_o_k': [0.956671, 0.765337, 0.612269], 'p_i': 40, 'u_i': 2.3676},
        {'id': 5, 'e_m': 0.734982, 'e_o_k': [0.421711, 0.337369, 0.269895], 'p_i': 10, 'u_i': 3.7622},
        {'id': 6, 'e_m': 0.370506, 'e_o_k': [0.212586, 0.170068, 0.136055], 'p_i': 10, 'u_i': 1.6504},
        {'id': 7, 'e_m': 7.686534, 'e_o_k': [4.410306, 3.528245, 2.822596], 'p_i': 80, 'u_i': 2.4020},
    ]
    B_BUDGET = 176.640008
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.123701, 'e_o_k': [0.644746, 0.515797, 0.412638], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 2.998422, 'e_o_k': [1.720406, 1.376325, 1.101060], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 12.570386, 'e_o_k': [7.212517, 5.770013, 4.616011], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.317492, 'e_o_k': [0.182167, 0.145734, 0.116587], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 2.758630, 'e_o_k': [1.582821, 1.266257, 1.013005], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 2.930909, 'e_o_k': [1.681669, 1.345335, 1.076268], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.031369, 'e_o_k': [0.017998, 0.014399, 0.011519], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.066594, 'e_o_k': [0.038210, 0.030568, 0.024454], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET

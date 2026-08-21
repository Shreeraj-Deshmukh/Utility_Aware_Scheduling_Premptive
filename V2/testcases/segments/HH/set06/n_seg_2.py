"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.123701, 'e_o_k': [0.873989, 0.699191], 'p_i': 10, 'u_i': 2.2300},
        {'id': 1, 'e_m': 2.998422, 'e_o_k': [2.332106, 1.865685], 'p_i': 20, 'u_i': 1.1980},
        {'id': 2, 'e_m': 12.570386, 'e_o_k': [9.776967, 7.821574], 'p_i': 40, 'u_i': 3.9540},
        {'id': 3, 'e_m': 0.317492, 'e_o_k': [0.246938, 0.197550], 'p_i': 80, 'u_i': 1.1604},
        {'id': 4, 'e_m': 2.758630, 'e_o_k': [2.145601, 1.716481], 'p_i': 40, 'u_i': 4.9556},
        {'id': 5, 'e_m': 2.930909, 'e_o_k': [2.279596, 1.823677], 'p_i': 20, 'u_i': 1.3741},
        {'id': 6, 'e_m': 0.031369, 'e_o_k': [0.024398, 0.019518], 'p_i': 10, 'u_i': 4.6107},
        {'id': 7, 'e_m': 0.066594, 'e_o_k': [0.051796, 0.041437], 'p_i': 80, 'u_i': 2.5105},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET

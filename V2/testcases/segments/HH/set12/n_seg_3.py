"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639983, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639983, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.147016, 'e_o_k': [0.658124, 0.526499, 0.421199], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 3.773755, 'e_o_k': [2.165269, 1.732216, 1.385772], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 5.350477, 'e_o_k': [3.069946, 2.455957, 1.964765], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 16.969247, 'e_o_k': [9.736453, 7.789162, 6.231330], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 1.099497, 'e_o_k': [0.630859, 0.504687, 0.403750], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.148964, 'e_o_k': [0.085471, 0.068377, 0.054702], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 3.297912, 'e_o_k': [1.892244, 1.513796, 1.211036], 'p_i': 80, 'u_i': 2.9271},
        {'id': 7, 'e_m': 3.766890, 'e_o_k': [2.161330, 1.729064, 1.383251], 'p_i': 80, 'u_i': 1.9023},
    ]
    B_BUDGET = 176.639983
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 25, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1012, "set": 12, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.573508, 'e_o_k': [0.446062, 0.356850], 'p_i': 10, 'u_i': 2.5980},
        {'id': 1, 'e_m': 1.886878, 'e_o_k': [1.467571, 1.174057], 'p_i': 20, 'u_i': 2.9083},
        {'id': 2, 'e_m': 2.675239, 'e_o_k': [2.080741, 1.664593], 'p_i': 40, 'u_i': 4.8275},
        {'id': 3, 'e_m': 8.484623, 'e_o_k': [6.599151, 5.279321], 'p_i': 80, 'u_i': 3.8825},
        {'id': 4, 'e_m': 0.549748, 'e_o_k': [0.427582, 0.342066], 'p_i': 20, 'u_i': 1.8333},
        {'id': 5, 'e_m': 0.074482, 'e_o_k': [0.057931, 0.046344], 'p_i': 20, 'u_i': 4.5368},
        {'id': 6, 'e_m': 1.648956, 'e_o_k': [1.282521, 1.026017], 'p_i': 80, 'u_i': 2.9271},
        {'id': 7, 'e_m': 1.883445, 'e_o_k': [1.464902, 1.171921], 'p_i': 80, 'u_i': 1.9023},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET

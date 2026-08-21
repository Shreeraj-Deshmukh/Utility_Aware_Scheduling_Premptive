"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639978, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639978, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.686544, 'e_o_k': [0.320387, 0.320387, 0.320387], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 1.582739, 'e_o_k': [1.107917, 1.107917], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 5.107137, 'e_o_k': [1.787498, 1.787498, 1.787498, 1.787498], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.225789, 'e_o_k': [0.079026, 0.079026, 0.079026, 0.079026], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 10.028404, 'e_o_k': [2.807953, 2.807953, 2.807953, 2.807953, 2.807953], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 5.390837, 'e_o_k': [1.257862, 1.257862, 1.257862, 1.257862, 1.257862, 1.257862], 'p_i': 40, 'u_i': 4.5618},
        {'id': 6, 'e_m': 0.266387, 'e_o_k': [0.186471, 0.186471], 'p_i': 10, 'u_i': 3.9189},
        {'id': 7, 'e_m': 4.383523, 'e_o_k': [1.534233, 1.534233, 1.534233, 1.534233], 'p_i': 40, 'u_i': 2.1344},
    ]
    B_BUDGET = 176.639978
    return processors, tasks, B_BUDGET

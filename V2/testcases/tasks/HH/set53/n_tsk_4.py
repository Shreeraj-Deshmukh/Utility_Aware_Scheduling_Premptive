"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.722559, 'e_o_k': [0.342677, 0.274142, 0.219313, 0.175451], 'p_i': 10, 'u_i': 3.6067},
        {'id': 1, 'e_m': 5.886831, 'e_o_k': [3.377690, 2.702152, 2.161722], 'p_i': 20, 'u_i': 2.3971},
        {'id': 2, 'e_m': 5.724986, 'e_o_k': [2.384275, 1.907420, 1.525936, 1.220749, 0.976599], 'p_i': 40, 'u_i': 3.3740},
        {'id': 3, 'e_m': 23.222228, 'e_o_k': [18.061733, 14.449386], 'p_i': 80, 'u_i': 3.0150},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET

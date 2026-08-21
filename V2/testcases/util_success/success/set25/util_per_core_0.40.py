"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680006, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680006, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.599440, 'e_o_k': [0.266573, 0.213259], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 5.185523, 'e_o_k': [0.637564, 0.510051, 0.408041], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 2.922224, 'e_o_k': [0.296974, 0.237579, 0.190063, 0.152051], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 7.584490, 'e_o_k': [1.264082, 1.011265], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 1.038987, 'e_o_k': [0.084487, 0.067590, 0.054072, 0.043257, 0.034606, 0.027685], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 1.421690, 'e_o_k': [0.115607, 0.092486, 0.073989, 0.059191, 0.047353, 0.037882], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 3.169787, 'e_o_k': [0.528298, 0.422638], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.366143, 'e_o_k': [0.045018, 0.036014, 0.028811], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 95.680006
    return processors, tasks, B_BUDGET

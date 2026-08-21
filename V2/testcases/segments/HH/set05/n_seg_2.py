"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640012, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640012, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.789693, 'e_o_k': [0.614206, 0.491365], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.245294, 'e_o_k': [0.190785, 0.152628], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 3.310794, 'e_o_k': [2.575062, 2.060050], 'p_i': 40, 'u_i': 2.1879},
        {'id': 3, 'e_m': 1.628519, 'e_o_k': [1.266626, 1.013301], 'p_i': 80, 'u_i': 2.3607},
        {'id': 4, 'e_m': 2.051152, 'e_o_k': [1.595340, 1.276272], 'p_i': 20, 'u_i': 2.0600},
        {'id': 5, 'e_m': 0.110349, 'e_o_k': [0.085827, 0.068662], 'p_i': 80, 'u_i': 2.1803},
        {'id': 6, 'e_m': 3.223708, 'e_o_k': [2.507328, 2.005863], 'p_i': 10, 'u_i': 4.5157},
        {'id': 7, 'e_m': 7.173276, 'e_o_k': [5.579215, 4.463372], 'p_i': 40, 'u_i': 4.4957},
    ]
    B_BUDGET = 176.640012
    return processors, tasks, B_BUDGET

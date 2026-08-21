"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.622274, 'e_o_k': [0.675626, 0.540501, 0.432401, 0.345920, 0.276736], 'p_i': 10, 'u_i': 4.0918},
        {'id': 1, 'e_m': 1.480680, 'e_o_k': [0.616656, 0.493325, 0.394660, 0.315728, 0.252582], 'p_i': 20, 'u_i': 2.7075},
        {'id': 2, 'e_m': 5.279637, 'e_o_k': [2.503893, 2.003114, 1.602491, 1.281993], 'p_i': 40, 'u_i': 3.4005},
        {'id': 3, 'e_m': 14.191480, 'e_o_k': [11.037818, 8.830254], 'p_i': 80, 'u_i': 3.5378},
        {'id': 4, 'e_m': 0.440421, 'e_o_k': [0.167130, 0.133704, 0.106963, 0.085571, 0.068456, 0.054765], 'p_i': 10, 'u_i': 2.8954},
        {'id': 5, 'e_m': 4.206242, 'e_o_k': [1.751766, 1.401413, 1.121131, 0.896904, 0.717524], 'p_i': 20, 'u_i': 2.6615},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET

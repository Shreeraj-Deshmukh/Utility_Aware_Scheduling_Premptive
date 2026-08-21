"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639987, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639987, "H": 80, "J": 19, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1020, "set": 20, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.830191, 'e_o_k': [1.178685, 0.942948, 0.754358, 0.603487, 0.482789], 'p_i': 10, 'u_i': 3.0842},
        {'id': 1, 'e_m': 1.814502, 'e_o_k': [0.860536, 0.688429, 0.550743, 0.440595], 'p_i': 20, 'u_i': 4.6180},
        {'id': 2, 'e_m': 4.430906, 'e_o_k': [1.845332, 1.476266, 1.181012, 0.944810, 0.755848], 'p_i': 40, 'u_i': 1.1953},
        {'id': 3, 'e_m': 14.541137, 'e_o_k': [8.343276, 6.674620, 5.339696], 'p_i': 80, 'u_i': 1.1811},
        {'id': 4, 'e_m': 1.174677, 'e_o_k': [0.489216, 0.391373, 0.313098, 0.250478, 0.200383], 'p_i': 40, 'u_i': 1.7367},
        {'id': 5, 'e_m': 4.174079, 'e_o_k': [1.583971, 1.267176, 1.013741, 0.810993, 0.648794, 0.519035], 'p_i': 40, 'u_i': 3.6203},
    ]
    B_BUDGET = 176.639987
    return processors, tasks, B_BUDGET

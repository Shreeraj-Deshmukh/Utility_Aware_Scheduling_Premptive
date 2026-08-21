"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319977, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319977, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.051709, 0.051709, 0.051709, 0.051709, 0.051709, 0.051709], 'p_i': 10, 'u_i': 3.7777},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.053905, 0.053905, 0.053905, 0.053905, 0.053905], 'p_i': 20, 'u_i': 2.9102},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [1.257717, 1.257717, 1.257717, 1.257717], 'p_i': 40, 'u_i': 3.0744},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [7.217249, 7.217249], 'p_i': 80, 'u_i': 3.1102},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.169346, 0.169346, 0.169346, 0.169346, 0.169346, 0.169346], 'p_i': 20, 'u_i': 3.9746},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.314137, 0.314137, 0.314137], 'p_i': 10, 'u_i': 1.5757},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.482519, 0.482519, 0.482519], 'p_i': 40, 'u_i': 4.9941},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.561227, 0.561227], 'p_i': 40, 'u_i': 1.7632},
    ]
    B_BUDGET = 88.319977
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.823643, 'e_o_k': [0.472582, 0.378066, 0.302453], 'p_i': 10, 'u_i': 2.3752},
        {'id': 1, 'e_m': 0.017150, 'e_o_k': [0.009840, 0.007872, 0.006298], 'p_i': 20, 'u_i': 4.5040},
        {'id': 2, 'e_m': 1.462946, 'e_o_k': [0.839395, 0.671516, 0.537213], 'p_i': 40, 'u_i': 4.7123},
        {'id': 3, 'e_m': 0.827621, 'e_o_k': [0.474864, 0.379892, 0.303913], 'p_i': 80, 'u_i': 4.3702},
        {'id': 4, 'e_m': 0.489062, 'e_o_k': [0.280609, 0.224488, 0.179590], 'p_i': 20, 'u_i': 3.7678},
        {'id': 5, 'e_m': 0.934156, 'e_o_k': [0.535991, 0.428793, 0.343034], 'p_i': 40, 'u_i': 3.2312},
        {'id': 6, 'e_m': 7.716508, 'e_o_k': [4.427505, 3.542004, 2.833603], 'p_i': 80, 'u_i': 3.7207},
        {'id': 7, 'e_m': 5.023836, 'e_o_k': [2.882529, 2.306023, 1.844818], 'p_i': 40, 'u_i': 2.0745},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET

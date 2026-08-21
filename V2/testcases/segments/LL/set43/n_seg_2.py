"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 26, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.025820, 'e_o_k': [0.007172, 0.005738], 'p_i': 10, 'u_i': 4.0574},
        {'id': 1, 'e_m': 1.233166, 'e_o_k': [0.342546, 0.274037], 'p_i': 20, 'u_i': 2.7090},
        {'id': 2, 'e_m': 1.873854, 'e_o_k': [0.520515, 0.416412], 'p_i': 40, 'u_i': 3.6072},
        {'id': 3, 'e_m': 2.076895, 'e_o_k': [0.576915, 0.461532], 'p_i': 80, 'u_i': 4.0494},
        {'id': 4, 'e_m': 0.193184, 'e_o_k': [0.053662, 0.042930], 'p_i': 20, 'u_i': 4.5815},
        {'id': 5, 'e_m': 2.190958, 'e_o_k': [0.608599, 0.486880], 'p_i': 20, 'u_i': 1.1362},
        {'id': 6, 'e_m': 0.888908, 'e_o_k': [0.246919, 0.197535], 'p_i': 80, 'u_i': 3.3217},
        {'id': 7, 'e_m': 5.305348, 'e_o_k': [1.473708, 1.178966], 'p_i': 40, 'u_i': 1.1761},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET

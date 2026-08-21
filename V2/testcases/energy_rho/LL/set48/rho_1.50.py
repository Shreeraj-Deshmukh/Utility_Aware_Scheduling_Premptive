"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 64.400007, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1048, "set": 48, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}
"""

_SPEC = '{"B": 64.400007, "H": 80, "J": 29, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.5, "seed": 1048, "set": 48, "sweep": "energy_rho", "util_per_core": 0.2, "value": "1.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.686006, 'e_o_k': [0.190557, 0.152446], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 1.744166, 'e_o_k': [0.357411, 0.285929, 0.228743], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.047982, 'e_o_k': [0.009832, 0.007866, 0.006293], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 1.929764, 'e_o_k': [0.536046, 0.428837], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 5.818863, 'e_o_k': [1.616351, 1.293081], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 1.092627, 'e_o_k': [0.162516, 0.130013, 0.104010, 0.083208, 0.066567], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 0.842076, 'e_o_k': [0.125249, 0.100199, 0.080160, 0.064128, 0.051302], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 0.583581, 'e_o_k': [0.086801, 0.069441, 0.055553, 0.044442, 0.035554], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 64.400007
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.404009, 'e_o_k': [0.082789, 0.066231, 0.052985], 'p_i': 10, 'u_i': 4.1044},
        {'id': 1, 'e_m': 1.312342, 'e_o_k': [0.268923, 0.215138, 0.172110], 'p_i': 20, 'u_i': 3.5158},
        {'id': 2, 'e_m': 1.516961, 'e_o_k': [0.310853, 0.248682, 0.198946], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 10.070496, 'e_o_k': [2.063626, 1.650901, 1.320721], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 1.082847, 'e_o_k': [0.221895, 0.177516, 0.142013], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.068047, 'e_o_k': [0.013944, 0.011155, 0.008924], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 1.937905, 'e_o_k': [0.397112, 0.317689, 0.254151], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.241844, 'e_o_k': [0.049558, 0.039647, 0.031717], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET

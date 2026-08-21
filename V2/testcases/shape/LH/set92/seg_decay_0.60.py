"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320017, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320017, "H": 80, "J": 34, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.279536, 'e_o_k': [0.169739, 0.101843, 0.061106, 0.036664, 0.021998], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 0.807491, 'e_o_k': [0.474325, 0.284595, 0.170757, 0.102454, 0.061473, 0.036884], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 3.179023, 'e_o_k': [2.270730, 1.362438, 0.817463], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 7.775197, 'e_o_k': [5.002425, 3.001455, 1.800873, 1.080524], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.001832, 'e_o_k': [0.001603, 0.000962], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 1.937647, 'e_o_k': [1.384034, 0.830420, 0.498252], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 0.361320, 'e_o_k': [0.232467, 0.139480, 0.083688, 0.050213], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 3.778825, 'e_o_k': [2.431229, 1.458737, 0.875242, 0.525145], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 88.320017
    return processors, tasks, B_BUDGET

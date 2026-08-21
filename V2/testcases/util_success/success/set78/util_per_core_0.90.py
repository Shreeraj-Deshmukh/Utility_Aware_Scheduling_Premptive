"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279991, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279991, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1078, "set": 78, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.802264, 'e_o_k': [0.488035, 0.390428, 0.312342, 0.249874], 'p_i': 10, 'u_i': 2.0207},
        {'id': 1, 'e_m': 5.425074, 'e_o_k': [0.551329, 0.441063, 0.352850, 0.282280], 'p_i': 20, 'u_i': 2.6196},
        {'id': 2, 'e_m': 15.951763, 'e_o_k': [1.961282, 1.569026, 1.255221], 'p_i': 40, 'u_i': 3.8291},
        {'id': 3, 'e_m': 1.375243, 'e_o_k': [0.111830, 0.089464, 0.071571, 0.057257, 0.045806, 0.036645], 'p_i': 80, 'u_i': 4.5678},
        {'id': 4, 'e_m': 3.854442, 'e_o_k': [0.473907, 0.379125, 0.303300], 'p_i': 10, 'u_i': 3.2870},
        {'id': 5, 'e_m': 0.011689, 'e_o_k': [0.000950, 0.000760, 0.000608, 0.000487, 0.000389, 0.000311], 'p_i': 20, 'u_i': 4.1768},
        {'id': 6, 'e_m': 0.284795, 'e_o_k': [0.023159, 0.018527, 0.014822, 0.011857, 0.009486, 0.007589], 'p_i': 10, 'u_i': 1.1477},
        {'id': 7, 'e_m': 2.180271, 'e_o_k': [0.268066, 0.214453, 0.171562], 'p_i': 10, 'u_i': 2.3697},
    ]
    B_BUDGET = 215.279991
    return processors, tasks, B_BUDGET

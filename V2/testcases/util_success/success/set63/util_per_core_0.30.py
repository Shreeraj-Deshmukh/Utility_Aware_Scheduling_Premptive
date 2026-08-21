"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760001, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760001, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.235465, 'e_o_k': [0.100464, 0.080371, 0.064297, 0.051438, 0.041150, 0.032920], 'p_i': 10, 'u_i': 3.9772},
        {'id': 1, 'e_m': 0.025725, 'e_o_k': [0.002614, 0.002091, 0.001673, 0.001339], 'p_i': 20, 'u_i': 1.4627},
        {'id': 2, 'e_m': 2.194419, 'e_o_k': [0.365736, 0.292589], 'p_i': 40, 'u_i': 4.5040},
        {'id': 3, 'e_m': 1.241431, 'e_o_k': [0.152635, 0.122108, 0.097686], 'p_i': 80, 'u_i': 4.7123},
        {'id': 4, 'e_m': 0.733593, 'e_o_k': [0.065468, 0.052375, 0.041900, 0.033520, 0.026816], 'p_i': 20, 'u_i': 4.3702},
        {'id': 5, 'e_m': 1.401234, 'e_o_k': [0.142402, 0.113921, 0.091137, 0.072910], 'p_i': 40, 'u_i': 3.7678},
        {'id': 6, 'e_m': 11.574762, 'e_o_k': [1.176297, 0.941038, 0.752830, 0.602264], 'p_i': 80, 'u_i': 3.2312},
        {'id': 7, 'e_m': 7.535753, 'e_o_k': [0.926527, 0.741222, 0.592977], 'p_i': 40, 'u_i': 3.7207},
    ]
    B_BUDGET = 71.760001
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 47, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 47, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "utility", "util_per_core": 0.2, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.612231, 'e_o_k': [0.232328, 0.185862, 0.148690, 0.118952, 0.095162, 0.076129], 'p_i': 10, 'u_i': 2.5421},
        {'id': 1, 'e_m': 0.818720, 'e_o_k': [0.310686, 0.248549, 0.198839, 0.159071, 0.127257, 0.101806], 'p_i': 20, 'u_i': 2.6843},
        {'id': 2, 'e_m': 1.130553, 'e_o_k': [0.429020, 0.343216, 0.274573, 0.219658, 0.175727, 0.140581], 'p_i': 40, 'u_i': 2.5504},
        {'id': 3, 'e_m': 0.013730, 'e_o_k': [0.010679, 0.008543], 'p_i': 80, 'u_i': 3.4451},
        {'id': 4, 'e_m': 0.810047, 'e_o_k': [0.464781, 0.371825, 0.297460], 'p_i': 10, 'u_i': 3.1766},
        {'id': 5, 'e_m': 1.453435, 'e_o_k': [1.130450, 0.904360], 'p_i': 10, 'u_i': 3.4349},
        {'id': 6, 'e_m': 0.030685, 'e_o_k': [0.023866, 0.019093], 'p_i': 10, 'u_i': 3.2708},
        {'id': 7, 'e_m': 0.399887, 'e_o_k': [0.166540, 0.133232, 0.106586, 0.085269, 0.068215], 'p_i': 10, 'u_i': 2.6100},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET

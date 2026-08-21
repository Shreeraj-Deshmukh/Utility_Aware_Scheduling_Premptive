"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.070595, 'e_o_k': [0.507735, 0.406188, 0.324950, 0.259960], 'p_i': 10, 'u_i': 2.6411},
        {'id': 1, 'e_m': 1.195922, 'e_o_k': [0.567172, 0.453737, 0.362990, 0.290392], 'p_i': 20, 'u_i': 4.9928},
        {'id': 2, 'e_m': 3.179254, 'e_o_k': [1.507776, 1.206221, 0.964977, 0.771981], 'p_i': 40, 'u_i': 3.9733},
        {'id': 3, 'e_m': 2.010249, 'e_o_k': [0.953370, 0.762696, 0.610157, 0.488126], 'p_i': 80, 'u_i': 1.2745},
        {'id': 4, 'e_m': 0.294507, 'e_o_k': [0.139671, 0.111737, 0.089390, 0.071512], 'p_i': 10, 'u_i': 1.8926},
        {'id': 5, 'e_m': 1.250085, 'e_o_k': [0.592859, 0.474287, 0.379430, 0.303544], 'p_i': 40, 'u_i': 4.4301},
        {'id': 6, 'e_m': 2.310377, 'e_o_k': [1.095707, 0.876566, 0.701253, 0.561002], 'p_i': 40, 'u_i': 2.8023},
        {'id': 7, 'e_m': 0.100727, 'e_o_k': [0.047770, 0.038216, 0.030573, 0.024458], 'p_i': 10, 'u_i': 1.0101},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET

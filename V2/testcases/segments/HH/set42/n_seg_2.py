"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.439153, 'e_o_k': [1.119342, 0.895473], 'p_i': 10, 'u_i': 3.9504},
        {'id': 1, 'e_m': 2.079360, 'e_o_k': [1.617280, 1.293824], 'p_i': 20, 'u_i': 2.1226},
        {'id': 2, 'e_m': 0.294327, 'e_o_k': [0.228921, 0.183137], 'p_i': 40, 'u_i': 2.4300},
        {'id': 3, 'e_m': 1.315035, 'e_o_k': [1.022805, 0.818244], 'p_i': 80, 'u_i': 4.3958},
        {'id': 4, 'e_m': 8.960451, 'e_o_k': [6.969240, 5.575392], 'p_i': 80, 'u_i': 3.0676},
        {'id': 5, 'e_m': 0.048915, 'e_o_k': [0.038045, 0.030436], 'p_i': 80, 'u_i': 1.8128},
        {'id': 6, 'e_m': 2.000915, 'e_o_k': [1.556267, 1.245014], 'p_i': 20, 'u_i': 1.5689},
        {'id': 7, 'e_m': 12.626309, 'e_o_k': [9.820462, 7.856370], 'p_i': 40, 'u_i': 4.8976},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET

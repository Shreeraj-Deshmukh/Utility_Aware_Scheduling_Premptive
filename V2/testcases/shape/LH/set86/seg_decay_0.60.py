"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32001, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.32001, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.050222, 'e_o_k': [0.035873, 0.021524, 0.012914], 'p_i': 10, 'u_i': 2.4144},
        {'id': 1, 'e_m': 0.206926, 'e_o_k': [0.181060, 0.108636], 'p_i': 20, 'u_i': 2.6559},
        {'id': 2, 'e_m': 1.190379, 'e_o_k': [0.722819, 0.433691, 0.260215, 0.156129, 0.093677], 'p_i': 40, 'u_i': 2.8681},
        {'id': 3, 'e_m': 6.971948, 'e_o_k': [6.100454, 3.660273], 'p_i': 80, 'u_i': 1.8896},
        {'id': 4, 'e_m': 0.550862, 'e_o_k': [0.334493, 0.200696, 0.120417, 0.072250, 0.043350], 'p_i': 20, 'u_i': 1.6645},
        {'id': 5, 'e_m': 0.291867, 'e_o_k': [0.177227, 0.106336, 0.063802, 0.038281, 0.022969], 'p_i': 40, 'u_i': 1.3774},
        {'id': 6, 'e_m': 1.611679, 'e_o_k': [1.410219, 0.846132], 'p_i': 80, 'u_i': 1.9412},
        {'id': 7, 'e_m': 17.018957, 'e_o_k': [14.891587, 8.934952], 'p_i': 80, 'u_i': 2.2237},
    ]
    B_BUDGET = 88.320010
    return processors, tasks, B_BUDGET

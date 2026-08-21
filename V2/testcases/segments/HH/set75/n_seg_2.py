"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64001, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.64001, "H": 80, "J": 36, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.893774, 'e_o_k': [0.695157, 0.556126], 'p_i': 10, 'u_i': 4.1325},
        {'id': 1, 'e_m': 0.002051, 'e_o_k': [0.001595, 0.001276], 'p_i': 20, 'u_i': 2.4718},
        {'id': 2, 'e_m': 13.125199, 'e_o_k': [10.208488, 8.166790], 'p_i': 40, 'u_i': 2.6491},
        {'id': 3, 'e_m': 4.683481, 'e_o_k': [3.642708, 2.914166], 'p_i': 80, 'u_i': 3.7785},
        {'id': 4, 'e_m': 0.355356, 'e_o_k': [0.276388, 0.221110], 'p_i': 10, 'u_i': 2.0110},
        {'id': 5, 'e_m': 0.683705, 'e_o_k': [0.531771, 0.425417], 'p_i': 10, 'u_i': 2.7392},
        {'id': 6, 'e_m': 12.075953, 'e_o_k': [9.392408, 7.513927], 'p_i': 80, 'u_i': 4.5700},
        {'id': 7, 'e_m': 1.379822, 'e_o_k': [1.073195, 0.858556], 'p_i': 20, 'u_i': 2.3393},
    ]
    B_BUDGET = 176.640010
    return processors, tasks, B_BUDGET

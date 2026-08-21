"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127808, 'e_o_k': [0.099406, 0.079525], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 4.638287, 'e_o_k': [3.607557, 2.886045], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.800790, 'e_o_k': [0.622837, 0.498269], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 9.437860, 'e_o_k': [7.340558, 5.872446], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 3.483129, 'e_o_k': [2.709100, 2.167280], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 14.523637, 'e_o_k': [11.296162, 9.036929], 'p_i': 80, 'u_i': 4.6158},
        {'id': 6, 'e_m': 0.073356, 'e_o_k': [0.057054, 0.045643], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 1.158844, 'e_o_k': [0.901323, 0.721059], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET

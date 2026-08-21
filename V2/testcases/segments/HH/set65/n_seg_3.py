"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640017, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640017, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.127808, 'e_o_k': [0.073332, 0.058666, 0.046933], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 4.638287, 'e_o_k': [2.661312, 2.129050, 1.703240], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.800790, 'e_o_k': [0.459470, 0.367576, 0.294061], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 9.437860, 'e_o_k': [5.415166, 4.332133, 3.465706], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 3.483129, 'e_o_k': [1.998517, 1.598813, 1.279051], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 14.523637, 'e_o_k': [8.333234, 6.666587, 5.333270], 'p_i': 80, 'u_i': 4.6158},
        {'id': 6, 'e_m': 0.073356, 'e_o_k': [0.042089, 0.033671, 0.026937], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 1.158844, 'e_o_k': [0.664911, 0.531929, 0.425543], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 176.640017
    return processors, tasks, B_BUDGET

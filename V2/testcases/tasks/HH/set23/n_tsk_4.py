"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.699186, 'e_o_k': [0.707657, 0.566126, 0.452901, 0.362321, 0.289856], 'p_i': 10, 'u_i': 2.2469},
        {'id': 1, 'e_m': 4.131054, 'e_o_k': [1.720453, 1.376362, 1.101090, 0.880872, 0.704698], 'p_i': 20, 'u_i': 2.3819},
        {'id': 2, 'e_m': 0.073268, 'e_o_k': [0.034748, 0.027798, 0.022238, 0.017791], 'p_i': 40, 'u_i': 2.4700},
        {'id': 3, 'e_m': 33.735759, 'e_o_k': [14.049876, 11.239901, 8.991921, 7.193536, 5.754829], 'p_i': 80, 'u_i': 2.1021},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET

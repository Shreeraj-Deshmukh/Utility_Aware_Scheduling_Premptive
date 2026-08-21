"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.19999, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.19999, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.066460, 'e_o_k': [0.009885, 0.007908, 0.006326, 0.005061, 0.004049], 'p_i': 10, 'u_i': 4.9998},
        {'id': 1, 'e_m': 0.732917, 'e_o_k': [0.203588, 0.162870], 'p_i': 20, 'u_i': 2.8601},
        {'id': 2, 'e_m': 0.018045, 'e_o_k': [0.003056, 0.002445, 0.001956, 0.001565], 'p_i': 40, 'u_i': 4.7969},
        {'id': 3, 'e_m': 2.107623, 'e_o_k': [0.313485, 0.250788, 0.200630, 0.160504, 0.128403], 'p_i': 80, 'u_i': 4.3760},
        {'id': 4, 'e_m': 7.862420, 'e_o_k': [1.611152, 1.288921, 1.031137], 'p_i': 80, 'u_i': 3.1042},
        {'id': 5, 'e_m': 18.530521, 'e_o_k': [2.511401, 2.009121, 1.607296, 1.285837, 1.028670, 0.822936], 'p_i': 80, 'u_i': 1.7042},
    ]
    B_BUDGET = 55.199990
    return processors, tasks, B_BUDGET

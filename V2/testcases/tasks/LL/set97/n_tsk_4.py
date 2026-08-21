"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.770853, 'e_o_k': [0.104472, 0.083578, 0.066862, 0.053490, 0.042792, 0.034233], 'p_i': 10, 'u_i': 4.6443},
        {'id': 1, 'e_m': 5.496848, 'e_o_k': [0.744976, 0.595981, 0.476784, 0.381428, 0.305142, 0.244114], 'p_i': 20, 'u_i': 3.3399},
        {'id': 2, 'e_m': 0.244179, 'e_o_k': [0.033093, 0.026474, 0.021180, 0.016944, 0.013555, 0.010844], 'p_i': 40, 'u_i': 3.1360},
        {'id': 3, 'e_m': 3.357422, 'e_o_k': [0.687996, 0.550397, 0.440318], 'p_i': 80, 'u_i': 4.9615},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET

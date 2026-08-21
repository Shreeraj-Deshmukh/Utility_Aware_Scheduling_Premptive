"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.103477, 'e_o_k': [0.164130, 0.131304, 0.105043, 0.084034, 0.067228], 'p_i': 10, 'u_i': 2.2919},
        {'id': 1, 'e_m': 0.023443, 'e_o_k': [0.003177, 0.002542, 0.002033, 0.001627, 0.001301, 0.001041], 'p_i': 20, 'u_i': 3.9772},
        {'id': 2, 'e_m': 2.133839, 'e_o_k': [0.361423, 0.289138, 0.231310, 0.185048], 'p_i': 40, 'u_i': 1.4627},
        {'id': 3, 'e_m': 1.363358, 'e_o_k': [0.378711, 0.302968], 'p_i': 80, 'u_i': 4.5040},
        {'id': 4, 'e_m': 1.081537, 'e_o_k': [0.221626, 0.177301, 0.141841], 'p_i': 20, 'u_i': 4.7123},
        {'id': 5, 'e_m': 6.560614, 'e_o_k': [0.975817, 0.780654, 0.624523, 0.499618, 0.399695], 'p_i': 40, 'u_i': 4.3702},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET

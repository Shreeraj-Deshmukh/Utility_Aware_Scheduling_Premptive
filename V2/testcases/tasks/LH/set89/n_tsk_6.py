"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.830029, 'e_o_k': [0.645578, 0.516462], 'p_i': 10, 'u_i': 3.8713},
        {'id': 1, 'e_m': 1.113681, 'e_o_k': [0.866197, 0.692957], 'p_i': 20, 'u_i': 1.2249},
        {'id': 2, 'e_m': 1.600304, 'e_o_k': [1.244681, 0.995745], 'p_i': 40, 'u_i': 3.9801},
        {'id': 3, 'e_m': 0.022536, 'e_o_k': [0.008552, 0.006842, 0.005473, 0.004379, 0.003503, 0.002802], 'p_i': 80, 'u_i': 1.7372},
        {'id': 4, 'e_m': 1.454332, 'e_o_k': [0.551887, 0.441509, 0.353208, 0.282566, 0.226053, 0.180842], 'p_i': 10, 'u_i': 1.2016},
        {'id': 5, 'e_m': 0.755905, 'e_o_k': [0.587926, 0.470341], 'p_i': 10, 'u_i': 4.7805},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 31, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.830029, 'e_o_k': [0.230564, 0.184451], 'p_i': 10, 'u_i': 3.8713},
        {'id': 1, 'e_m': 1.113681, 'e_o_k': [0.309356, 0.247485], 'p_i': 20, 'u_i': 1.2249},
        {'id': 2, 'e_m': 1.600304, 'e_o_k': [0.444529, 0.355623], 'p_i': 40, 'u_i': 3.9801},
        {'id': 3, 'e_m': 0.022536, 'e_o_k': [0.003054, 0.002443, 0.001955, 0.001564, 0.001251, 0.001001], 'p_i': 80, 'u_i': 1.7372},
        {'id': 4, 'e_m': 1.454332, 'e_o_k': [0.197102, 0.157682, 0.126146, 0.100916, 0.080733, 0.064587], 'p_i': 10, 'u_i': 1.2016},
        {'id': 5, 'e_m': 0.755905, 'e_o_k': [0.209974, 0.167979], 'p_i': 10, 'u_i': 4.7805},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET

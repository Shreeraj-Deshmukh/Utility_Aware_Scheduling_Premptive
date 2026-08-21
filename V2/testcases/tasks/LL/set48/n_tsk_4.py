"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.421261, 'e_o_k': [0.394795, 0.315836], 'p_i': 10, 'u_i': 2.1906},
        {'id': 1, 'e_m': 3.094134, 'e_o_k': [0.460217, 0.368174, 0.294539, 0.235631, 0.188505], 'p_i': 20, 'u_i': 4.5509},
        {'id': 2, 'e_m': 0.100368, 'e_o_k': [0.014929, 0.011943, 0.009554, 0.007643, 0.006115], 'p_i': 40, 'u_i': 2.6037},
        {'id': 3, 'e_m': 8.052642, 'e_o_k': [2.236845, 1.789476], 'p_i': 80, 'u_i': 2.6419},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET

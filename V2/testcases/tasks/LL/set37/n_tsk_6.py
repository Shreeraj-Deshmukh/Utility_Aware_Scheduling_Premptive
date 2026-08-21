"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.561109, 'e_o_k': [0.319899, 0.255919, 0.204736], 'p_i': 10, 'u_i': 4.5515},
        {'id': 1, 'e_m': 0.460144, 'e_o_k': [0.127818, 0.102254], 'p_i': 20, 'u_i': 3.0521},
        {'id': 2, 'e_m': 1.133580, 'e_o_k': [0.192002, 0.153602, 0.122881, 0.098305], 'p_i': 40, 'u_i': 1.1668},
        {'id': 3, 'e_m': 12.114088, 'e_o_k': [3.365024, 2.692019], 'p_i': 80, 'u_i': 2.3448},
        {'id': 4, 'e_m': 1.064930, 'e_o_k': [0.158396, 0.126717, 0.101374, 0.081099, 0.064879], 'p_i': 40, 'u_i': 3.9461},
        {'id': 5, 'e_m': 0.289862, 'e_o_k': [0.049096, 0.039277, 0.031421, 0.025137], 'p_i': 20, 'u_i': 2.2173},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.291918, 'e_o_k': [0.081088, 0.064871], 'p_i': 10, 'u_i': 3.2224},
        {'id': 1, 'e_m': 5.620499, 'e_o_k': [0.835986, 0.668789, 0.535031, 0.428025, 0.342420], 'p_i': 20, 'u_i': 4.1436},
        {'id': 2, 'e_m': 0.861058, 'e_o_k': [0.128073, 0.102458, 0.081967, 0.065573, 0.052459], 'p_i': 40, 'u_i': 3.8879},
        {'id': 3, 'e_m': 5.460544, 'e_o_k': [0.740056, 0.592044, 0.473636, 0.378908, 0.303127, 0.242501], 'p_i': 80, 'u_i': 3.5961},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.928215, 'e_o_k': [0.257838, 0.206270], 'p_i': 10, 'u_i': 3.9192},
        {'id': 1, 'e_m': 2.294677, 'e_o_k': [0.637410, 0.509928], 'p_i': 20, 'u_i': 2.9693},
        {'id': 2, 'e_m': 2.441425, 'e_o_k': [0.330881, 0.264705, 0.211764, 0.169411, 0.135529, 0.108423], 'p_i': 40, 'u_i': 2.3800},
        {'id': 3, 'e_m': 10.512720, 'e_o_k': [1.780610, 1.424488, 1.139590, 0.911672], 'p_i': 80, 'u_i': 3.7938},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET

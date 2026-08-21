"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.301374, 'e_o_k': [0.061757, 0.049406, 0.039524], 'p_i': 10, 'u_i': 4.0696},
        {'id': 1, 'e_m': 2.535370, 'e_o_k': [0.704269, 0.563416], 'p_i': 20, 'u_i': 1.5844},
        {'id': 2, 'e_m': 1.148643, 'e_o_k': [0.319068, 0.255254], 'p_i': 40, 'u_i': 4.9877},
        {'id': 3, 'e_m': 13.128461, 'e_o_k': [3.646795, 2.917436], 'p_i': 80, 'u_i': 3.4936},
        {'id': 4, 'e_m': 0.398978, 'e_o_k': [0.067578, 0.054062, 0.043250, 0.034600], 'p_i': 80, 'u_i': 4.0270},
        {'id': 5, 'e_m': 0.452850, 'e_o_k': [0.076702, 0.061362, 0.049089, 0.039272], 'p_i': 10, 'u_i': 3.7051},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET

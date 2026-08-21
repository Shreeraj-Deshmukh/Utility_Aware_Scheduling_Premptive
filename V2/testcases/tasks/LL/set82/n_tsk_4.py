"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.700591, 'e_o_k': [0.252944, 0.202355, 0.161884, 0.129507, 0.103606], 'p_i': 10, 'u_i': 2.1126},
        {'id': 1, 'e_m': 0.377443, 'e_o_k': [0.063930, 0.051144, 0.040915, 0.032732], 'p_i': 20, 'u_i': 1.1880},
        {'id': 2, 'e_m': 3.907664, 'e_o_k': [1.085462, 0.868370], 'p_i': 40, 'u_i': 4.0095},
        {'id': 3, 'e_m': 9.070175, 'e_o_k': [1.349086, 1.079269, 0.863415, 0.690732, 0.552586], 'p_i': 80, 'u_i': 4.5444},
    ]
    B_BUDGET = 55.200008
    return processors, tasks, B_BUDGET

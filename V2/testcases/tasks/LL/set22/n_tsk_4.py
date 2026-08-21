"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.961172, 'e_o_k': [0.291702, 0.233362, 0.186689, 0.149352, 0.119481], 'p_i': 10, 'u_i': 3.1771},
        {'id': 1, 'e_m': 0.145065, 'e_o_k': [0.040296, 0.032237], 'p_i': 20, 'u_i': 3.8810},
        {'id': 2, 'e_m': 5.025013, 'e_o_k': [0.851120, 0.680896, 0.544717, 0.435774], 'p_i': 40, 'u_i': 1.9496},
        {'id': 3, 'e_m': 5.680334, 'e_o_k': [1.577871, 1.262297], 'p_i': 80, 'u_i': 4.0364},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET

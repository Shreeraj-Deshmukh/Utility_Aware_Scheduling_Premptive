"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1093, "set": 93, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.210650, 'e_o_k': [0.574157, 0.459325, 0.367460, 0.293968], 'p_i': 10, 'u_i': 4.8908},
        {'id': 1, 'e_m': 1.270017, 'e_o_k': [0.528922, 0.423138, 0.338510, 0.270808, 0.216646], 'p_i': 20, 'u_i': 3.7143},
        {'id': 2, 'e_m': 2.460196, 'e_o_k': [1.024594, 0.819675, 0.655740, 0.524592, 0.419674], 'p_i': 40, 'u_i': 4.3200},
        {'id': 3, 'e_m': 12.314336, 'e_o_k': [4.673018, 3.738414, 2.990731, 2.392585, 1.914068, 1.531254], 'p_i': 80, 'u_i': 3.1069},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET

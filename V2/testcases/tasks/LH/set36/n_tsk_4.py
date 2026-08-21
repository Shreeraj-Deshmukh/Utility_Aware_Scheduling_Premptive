"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.014200, 'e_o_k': [0.788822, 0.631058], 'p_i': 10, 'u_i': 1.1535},
        {'id': 1, 'e_m': 0.866375, 'e_o_k': [0.410882, 0.328706, 0.262965, 0.210372], 'p_i': 20, 'u_i': 2.8332},
        {'id': 2, 'e_m': 1.359317, 'e_o_k': [1.057247, 0.845797], 'p_i': 40, 'u_i': 2.4233},
        {'id': 3, 'e_m': 17.702265, 'e_o_k': [6.717617, 5.374094, 4.299275, 3.439420, 2.751536, 2.201229], 'p_i': 80, 'u_i': 4.2523},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET

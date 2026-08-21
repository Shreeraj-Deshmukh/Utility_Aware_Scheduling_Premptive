"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.616783, 'e_o_k': [1.241022, 0.992817, 0.794254, 0.635403], 'p_i': 10, 'u_i': 4.9199},
        {'id': 1, 'e_m': 2.666317, 'e_o_k': [1.264514, 1.011611, 0.809289, 0.647431], 'p_i': 20, 'u_i': 1.0213},
        {'id': 2, 'e_m': 12.394015, 'e_o_k': [5.877920, 4.702336, 3.761869, 3.009495], 'p_i': 40, 'u_i': 3.4352},
        {'id': 3, 'e_m': 7.612437, 'e_o_k': [3.610234, 2.888188, 2.310550, 1.848440], 'p_i': 80, 'u_i': 3.4020},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET

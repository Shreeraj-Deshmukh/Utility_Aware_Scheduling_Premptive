"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640021, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640021, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.692444, 'e_o_k': [0.802650, 0.642120, 0.513696, 0.410957], 'p_i': 10, 'u_i': 3.4352},
        {'id': 1, 'e_m': 1.673009, 'e_o_k': [0.793432, 0.634746, 0.507797, 0.406237], 'p_i': 20, 'u_i': 3.4020},
        {'id': 2, 'e_m': 8.380439, 'e_o_k': [4.808449, 3.846759, 3.077407], 'p_i': 40, 'u_i': 3.4221},
        {'id': 3, 'e_m': 10.582022, 'e_o_k': [4.407077, 3.525662, 2.820529, 2.256423, 1.805139], 'p_i': 80, 'u_i': 3.9841},
        {'id': 4, 'e_m': 1.210474, 'e_o_k': [0.694535, 0.555628, 0.444502], 'p_i': 40, 'u_i': 2.4868},
        {'id': 5, 'e_m': 1.750571, 'e_o_k': [0.664303, 0.531442, 0.425154, 0.340123, 0.272098, 0.217679], 'p_i': 10, 'u_i': 2.1829},
    ]
    B_BUDGET = 176.640021
    return processors, tasks, B_BUDGET

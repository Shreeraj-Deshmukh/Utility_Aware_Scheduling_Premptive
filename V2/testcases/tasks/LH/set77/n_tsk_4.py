"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.493963, 'e_o_k': [0.205720, 0.164576, 0.131661, 0.105329, 0.084263], 'p_i': 10, 'u_i': 1.8790},
        {'id': 1, 'e_m': 3.730438, 'e_o_k': [1.553609, 1.242888, 0.994310, 0.795448, 0.636358], 'p_i': 20, 'u_i': 3.3534},
        {'id': 2, 'e_m': 4.298707, 'e_o_k': [2.466471, 1.973177, 1.578542], 'p_i': 40, 'u_i': 2.5184},
        {'id': 3, 'e_m': 4.529127, 'e_o_k': [1.886238, 1.508990, 1.207192, 0.965754, 0.772603], 'p_i': 80, 'u_i': 4.2996},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET

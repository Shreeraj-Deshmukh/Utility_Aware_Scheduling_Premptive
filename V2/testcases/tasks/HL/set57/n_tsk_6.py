"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.280655, 'e_o_k': [0.077960, 0.062368], 'p_i': 10, 'u_i': 2.3979},
        {'id': 1, 'e_m': 2.090524, 'e_o_k': [0.580701, 0.464561], 'p_i': 20, 'u_i': 4.6396},
        {'id': 2, 'e_m': 12.172179, 'e_o_k': [1.810474, 1.448379, 1.158703, 0.926963, 0.741570], 'p_i': 40, 'u_i': 4.1139},
        {'id': 3, 'e_m': 11.670243, 'e_o_k': [1.581642, 1.265314, 1.012251, 0.809801, 0.647841, 0.518273], 'p_i': 80, 'u_i': 3.3967},
        {'id': 4, 'e_m': 13.518020, 'e_o_k': [3.755006, 3.004005], 'p_i': 80, 'u_i': 1.9449},
        {'id': 5, 'e_m': 1.930021, 'e_o_k': [0.536117, 0.428894], 'p_i': 40, 'u_i': 4.6056},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET

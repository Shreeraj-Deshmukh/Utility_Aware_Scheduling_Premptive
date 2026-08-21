"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.4, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.4, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.727022, 'e_o_k': [0.405614, 0.324491, 0.259593, 0.207674, 0.166139], 'p_i': 10, 'u_i': 4.2653},
        {'id': 1, 'e_m': 0.448204, 'e_o_k': [0.060744, 0.048595, 0.038876, 0.031101, 0.024881, 0.019905], 'p_i': 20, 'u_i': 3.8195},
        {'id': 2, 'e_m': 17.274833, 'e_o_k': [2.341220, 1.872976, 1.498381, 1.198705, 0.958964, 0.767171], 'p_i': 40, 'u_i': 1.2105},
        {'id': 3, 'e_m': 1.336713, 'e_o_k': [0.273917, 0.219133, 0.175307], 'p_i': 80, 'u_i': 1.7971},
        {'id': 4, 'e_m': 0.367997, 'e_o_k': [0.075409, 0.060327, 0.048262], 'p_i': 20, 'u_i': 3.9776},
        {'id': 5, 'e_m': 1.516321, 'e_o_k': [0.225536, 0.180428, 0.144343, 0.115474, 0.092379], 'p_i': 40, 'u_i': 2.5595},
    ]
    B_BUDGET = 110.400000
    return processors, tasks, B_BUDGET

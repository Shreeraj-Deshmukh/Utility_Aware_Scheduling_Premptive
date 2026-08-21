"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.165446, 'e_o_k': [0.024608, 0.019687, 0.015749, 0.012599, 0.010080], 'p_i': 10, 'u_i': 3.5312},
        {'id': 1, 'e_m': 1.641715, 'e_o_k': [0.222498, 0.177998, 0.142399, 0.113919, 0.091135, 0.072908], 'p_i': 20, 'u_i': 1.4207},
        {'id': 2, 'e_m': 5.181947, 'e_o_k': [0.770756, 0.616605, 0.493284, 0.394627, 0.315702], 'p_i': 40, 'u_i': 4.1417},
        {'id': 3, 'e_m': 10.738436, 'e_o_k': [1.597221, 1.277777, 1.022221, 0.817777, 0.654222], 'p_i': 80, 'u_i': 4.9795},
        {'id': 4, 'e_m': 0.202795, 'e_o_k': [0.041556, 0.033245, 0.026596], 'p_i': 20, 'u_i': 4.9448},
        {'id': 5, 'e_m': 0.274508, 'e_o_k': [0.040830, 0.032664, 0.026131, 0.020905, 0.016724], 'p_i': 10, 'u_i': 4.4554},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600016, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600016, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.698840, 'e_o_k': [0.062367, 0.049893, 0.039915, 0.031932, 0.025545], 'p_i': 10, 'u_i': 3.7403},
        {'id': 1, 'e_m': 2.018727, 'e_o_k': [0.164156, 0.131325, 0.105060, 0.084048, 0.067238, 0.053791], 'p_i': 20, 'u_i': 1.1622},
        {'id': 2, 'e_m': 7.947557, 'e_o_k': [0.977159, 0.781727, 0.625382], 'p_i': 40, 'u_i': 4.1752},
        {'id': 3, 'e_m': 19.437993, 'e_o_k': [1.975406, 1.580325, 1.264260, 1.011408], 'p_i': 80, 'u_i': 1.9420},
        {'id': 4, 'e_m': 0.004580, 'e_o_k': [0.000763, 0.000611], 'p_i': 10, 'u_i': 2.5093},
        {'id': 5, 'e_m': 4.844117, 'e_o_k': [0.595588, 0.476471, 0.381176], 'p_i': 80, 'u_i': 3.6510},
        {'id': 6, 'e_m': 0.903299, 'e_o_k': [0.091799, 0.073439, 0.058751, 0.047001], 'p_i': 10, 'u_i': 3.1983},
        {'id': 7, 'e_m': 9.447062, 'e_o_k': [0.960067, 0.768054, 0.614443, 0.491554], 'p_i': 40, 'u_i': 4.3627},
    ]
    B_BUDGET = 119.600016
    return processors, tasks, B_BUDGET

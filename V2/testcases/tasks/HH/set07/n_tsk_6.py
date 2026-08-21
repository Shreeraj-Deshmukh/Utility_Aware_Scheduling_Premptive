"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639986, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639986, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.245057, 'e_o_k': [0.092994, 0.074395, 0.059516, 0.047613, 0.038090, 0.030472], 'p_i': 10, 'u_i': 4.9047},
        {'id': 1, 'e_m': 0.839324, 'e_o_k': [0.481579, 0.385263, 0.308211], 'p_i': 20, 'u_i': 3.2321},
        {'id': 2, 'e_m': 4.678797, 'e_o_k': [1.948571, 1.558857, 1.247085, 0.997668, 0.798135], 'p_i': 40, 'u_i': 3.3144},
        {'id': 3, 'e_m': 2.870116, 'e_o_k': [1.089146, 0.871316, 0.697053, 0.557642, 0.446114, 0.356891], 'p_i': 80, 'u_i': 1.1307},
        {'id': 4, 'e_m': 3.001449, 'e_o_k': [1.250008, 1.000007, 0.800005, 0.640004, 0.512003], 'p_i': 20, 'u_i': 4.3260},
        {'id': 5, 'e_m': 8.612185, 'e_o_k': [4.941418, 3.953134, 3.162507], 'p_i': 20, 'u_i': 4.7000},
    ]
    B_BUDGET = 176.639986
    return processors, tasks, B_BUDGET

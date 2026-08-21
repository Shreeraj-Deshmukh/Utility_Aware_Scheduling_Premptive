"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.461036, 'e_o_k': [0.217313, 0.173850, 0.139080, 0.111264, 0.089011], 'p_i': 10, 'u_i': 1.1399},
        {'id': 1, 'e_m': 2.740078, 'e_o_k': [0.371357, 0.297085, 0.237668, 0.190135, 0.152108, 0.121686], 'p_i': 20, 'u_i': 4.6324},
        {'id': 2, 'e_m': 6.123017, 'e_o_k': [0.910730, 0.728584, 0.582867, 0.466294, 0.373035], 'p_i': 40, 'u_i': 3.3557},
        {'id': 3, 'e_m': 7.319613, 'e_o_k': [1.088710, 0.870968, 0.696774, 0.557419, 0.445935], 'p_i': 80, 'u_i': 3.4396},
        {'id': 4, 'e_m': 0.971590, 'e_o_k': [0.131677, 0.105342, 0.084274, 0.067419, 0.053935, 0.043148], 'p_i': 10, 'u_i': 2.9972},
        {'id': 5, 'e_m': 7.006514, 'e_o_k': [1.946254, 1.557003], 'p_i': 40, 'u_i': 3.3467},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET

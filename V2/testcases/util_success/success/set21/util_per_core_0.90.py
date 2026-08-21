"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280003, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280003, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.555745, 'e_o_k': [0.191280, 0.153024, 0.122419], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 8.215149, 'e_o_k': [0.668029, 0.534423, 0.427538, 0.342031, 0.273625, 0.218900], 'p_i': 20, 'u_i': 1.0830},
        {'id': 2, 'e_m': 12.081847, 'e_o_k': [2.013641, 1.610913], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 21.720827, 'e_o_k': [1.766265, 1.413012, 1.130410, 0.904328, 0.723462, 0.578770], 'p_i': 80, 'u_i': 2.8864},
        {'id': 4, 'e_m': 1.702828, 'e_o_k': [0.151966, 0.121573, 0.097258, 0.077807, 0.062245], 'p_i': 10, 'u_i': 1.3892},
        {'id': 5, 'e_m': 1.686691, 'e_o_k': [0.171412, 0.137129, 0.109703, 0.087763], 'p_i': 10, 'u_i': 2.4866},
        {'id': 6, 'e_m': 15.184409, 'e_o_k': [1.355105, 1.084084, 0.867268, 0.693814, 0.555051], 'p_i': 80, 'u_i': 4.5153},
        {'id': 7, 'e_m': 5.254182, 'e_o_k': [0.468900, 0.375120, 0.300096, 0.240077, 0.192061], 'p_i': 40, 'u_i': 1.1207},
    ]
    B_BUDGET = 215.280003
    return processors, tasks, B_BUDGET

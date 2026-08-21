"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639987, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639987, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.201315, 'e_o_k': [1.836820, 1.469456, 1.175565], 'p_i': 10, 'u_i': 1.6704},
        {'id': 1, 'e_m': 2.963590, 'e_o_k': [1.234241, 0.987393, 0.789915, 0.631932, 0.505545], 'p_i': 20, 'u_i': 3.6515},
        {'id': 2, 'e_m': 3.000662, 'e_o_k': [1.423078, 1.138463, 0.910770, 0.728616], 'p_i': 40, 'u_i': 1.3011},
        {'id': 3, 'e_m': 20.533791, 'e_o_k': [9.738248, 7.790598, 6.232479, 4.985983], 'p_i': 80, 'u_i': 4.8603},
    ]
    B_BUDGET = 176.639987
    return processors, tasks, B_BUDGET

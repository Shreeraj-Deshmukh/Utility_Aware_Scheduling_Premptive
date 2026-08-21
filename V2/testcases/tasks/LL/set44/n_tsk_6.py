"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200001, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.176605, 'e_o_k': [0.036189, 0.028952, 0.023161], 'p_i': 10, 'u_i': 4.9794},
        {'id': 1, 'e_m': 1.736478, 'e_o_k': [0.235341, 0.188273, 0.150618, 0.120495, 0.096396, 0.077117], 'p_i': 20, 'u_i': 1.8563},
        {'id': 2, 'e_m': 1.065864, 'e_o_k': [0.144454, 0.115563, 0.092451, 0.073961, 0.059168, 0.047335], 'p_i': 40, 'u_i': 1.0975},
        {'id': 3, 'e_m': 7.139651, 'e_o_k': [1.209291, 0.967432, 0.773946, 0.619157], 'p_i': 80, 'u_i': 4.1970},
        {'id': 4, 'e_m': 0.460507, 'e_o_k': [0.062411, 0.049929, 0.039943, 0.031955, 0.025564, 0.020451], 'p_i': 10, 'u_i': 1.7417},
        {'id': 5, 'e_m': 2.671454, 'e_o_k': [0.397349, 0.317879, 0.254303, 0.203442, 0.162754], 'p_i': 20, 'u_i': 3.7063},
    ]
    B_BUDGET = 55.200001
    return processors, tasks, B_BUDGET

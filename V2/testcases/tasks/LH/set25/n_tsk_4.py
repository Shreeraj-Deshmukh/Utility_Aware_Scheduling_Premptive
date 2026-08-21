"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.623021, 'e_o_k': [0.931242, 0.744993, 0.595995], 'p_i': 10, 'u_i': 3.5371},
        {'id': 1, 'e_m': 3.752982, 'e_o_k': [2.153351, 1.722680, 1.378144], 'p_i': 20, 'u_i': 2.5364},
        {'id': 2, 'e_m': 1.311882, 'e_o_k': [0.622166, 0.497733, 0.398186, 0.318549], 'p_i': 40, 'u_i': 2.9162},
        {'id': 3, 'e_m': 1.380136, 'e_o_k': [0.654536, 0.523629, 0.418903, 0.335123], 'p_i': 80, 'u_i': 1.5428},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET

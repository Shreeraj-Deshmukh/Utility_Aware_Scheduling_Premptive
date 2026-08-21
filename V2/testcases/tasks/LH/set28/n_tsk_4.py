"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319988, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319988, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.906412, 'e_o_k': [0.429870, 0.343896, 0.275117, 0.220094], 'p_i': 10, 'u_i': 4.1031},
        {'id': 1, 'e_m': 2.305692, 'e_o_k': [1.322938, 1.058351, 0.846680], 'p_i': 20, 'u_i': 2.8661},
        {'id': 2, 'e_m': 2.876100, 'e_o_k': [1.091416, 0.873133, 0.698506, 0.558805, 0.447044, 0.357635], 'p_i': 40, 'u_i': 2.5404},
        {'id': 3, 'e_m': 9.773732, 'e_o_k': [5.607879, 4.486303, 3.589042], 'p_i': 80, 'u_i': 1.0986},
    ]
    B_BUDGET = 88.319988
    return processors, tasks, B_BUDGET

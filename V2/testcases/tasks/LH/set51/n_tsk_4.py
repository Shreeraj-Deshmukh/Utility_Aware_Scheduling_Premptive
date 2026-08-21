"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1051, "set": 51, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.556454, 'e_o_k': [1.466818, 1.173454, 0.938763], 'p_i': 10, 'u_i': 2.0401},
        {'id': 1, 'e_m': 1.904091, 'e_o_k': [0.792994, 0.634395, 0.507516, 0.406013, 0.324810], 'p_i': 20, 'u_i': 1.0378},
        {'id': 2, 'e_m': 1.038996, 'e_o_k': [0.432709, 0.346167, 0.276934, 0.221547, 0.177238], 'p_i': 40, 'u_i': 1.8577},
        {'id': 3, 'e_m': 1.854010, 'e_o_k': [1.063776, 0.851021, 0.680817], 'p_i': 80, 'u_i': 4.0468},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET

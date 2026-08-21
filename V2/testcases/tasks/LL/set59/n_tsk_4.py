"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.613895, 'e_o_k': [0.726082, 0.580866], 'p_i': 10, 'u_i': 2.6714},
        {'id': 1, 'e_m': 0.628503, 'e_o_k': [0.106454, 0.085163, 0.068130, 0.054504], 'p_i': 20, 'u_i': 1.4256},
        {'id': 2, 'e_m': 3.259886, 'e_o_k': [0.905524, 0.724419], 'p_i': 40, 'u_i': 3.1325},
        {'id': 3, 'e_m': 2.055056, 'e_o_k': [0.570849, 0.456679], 'p_i': 80, 'u_i': 4.7073},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.489567, 'e_o_k': [0.380774, 0.304620], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 3.987962, 'e_o_k': [1.660860, 1.328688, 1.062950, 0.850360, 0.680288], 'p_i': 20, 'u_i': 4.6903},
        {'id': 2, 'e_m': 1.905685, 'e_o_k': [1.093426, 0.874741, 0.699793], 'p_i': 40, 'u_i': 4.0696},
        {'id': 3, 'e_m': 8.320245, 'e_o_k': [6.471302, 5.177041], 'p_i': 80, 'u_i': 1.5844},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET

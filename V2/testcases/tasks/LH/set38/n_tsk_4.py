"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.066228, 'e_o_k': [0.860519, 0.688415, 0.550732, 0.440586, 0.352468], 'p_i': 10, 'u_i': 1.1882},
        {'id': 1, 'e_m': 1.917825, 'e_o_k': [0.798714, 0.638971, 0.511177, 0.408941, 0.327153], 'p_i': 20, 'u_i': 4.0368},
        {'id': 2, 'e_m': 3.414456, 'e_o_k': [2.655688, 2.124550], 'p_i': 40, 'u_i': 1.1650},
        {'id': 3, 'e_m': 0.969960, 'e_o_k': [0.460008, 0.368007, 0.294405, 0.235524], 'p_i': 80, 'u_i': 2.0635},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET

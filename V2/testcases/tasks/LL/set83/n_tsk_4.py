"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.600658, 'e_o_k': [0.328004, 0.262403, 0.209922], 'p_i': 10, 'u_i': 1.6704},
        {'id': 1, 'e_m': 1.481795, 'e_o_k': [0.220400, 0.176320, 0.141056, 0.112845, 0.090276], 'p_i': 20, 'u_i': 3.6515},
        {'id': 2, 'e_m': 1.500331, 'e_o_k': [0.254121, 0.203297, 0.162638, 0.130110], 'p_i': 40, 'u_i': 1.3011},
        {'id': 3, 'e_m': 10.266896, 'e_o_k': [1.738973, 1.391178, 1.112943, 0.890354], 'p_i': 80, 'u_i': 4.8603},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.509866, 'e_o_k': [0.716061, 0.572849, 0.458279, 0.366623], 'p_i': 10, 'u_i': 3.2224},
        {'id': 1, 'e_m': 5.553953, 'e_o_k': [4.319741, 3.455793], 'p_i': 20, 'u_i': 2.5978},
        {'id': 2, 'e_m': 0.146404, 'e_o_k': [0.084002, 0.067202, 0.053761], 'p_i': 40, 'u_i': 4.5124},
        {'id': 3, 'e_m': 29.412456, 'e_o_k': [13.948997, 11.159197, 8.927358, 7.141886], 'p_i': 80, 'u_i': 4.6729},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET

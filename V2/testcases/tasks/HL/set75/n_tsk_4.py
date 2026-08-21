"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1075, "set": 75, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.589869, 'e_o_k': [0.269287, 0.215429, 0.172344, 0.137875], 'p_i': 10, 'u_i': 2.2754},
        {'id': 1, 'e_m': 2.051152, 'e_o_k': [0.569764, 0.455812], 'p_i': 20, 'u_i': 1.2102},
        {'id': 2, 'e_m': 9.003988, 'e_o_k': [1.845079, 1.476064, 1.180851], 'p_i': 40, 'u_i': 3.7306},
        {'id': 3, 'e_m': 25.068465, 'e_o_k': [5.136981, 4.109584, 3.287668], 'p_i': 80, 'u_i': 4.1325},
    ]
    B_BUDGET = 110.400007
    return processors, tasks, B_BUDGET

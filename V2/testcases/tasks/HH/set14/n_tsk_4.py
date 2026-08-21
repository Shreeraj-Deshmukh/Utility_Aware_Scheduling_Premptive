"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1014, "set": 14, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.585280, 'e_o_k': [0.660219, 0.528175, 0.422540, 0.338032, 0.270426], 'p_i': 10, 'u_i': 3.7039},
        {'id': 1, 'e_m': 6.553932, 'e_o_k': [2.487072, 1.989657, 1.591726, 1.273381, 1.018705, 0.814964], 'p_i': 20, 'u_i': 3.4878},
        {'id': 2, 'e_m': 12.113109, 'e_o_k': [5.044727, 4.035781, 3.228625, 2.582900, 2.066320], 'p_i': 40, 'u_i': 4.7761},
        {'id': 3, 'e_m': 0.875811, 'e_o_k': [0.364748, 0.291798, 0.233438, 0.186751, 0.149401], 'p_i': 80, 'u_i': 2.0030},
    ]
    B_BUDGET = 176.639994
    return processors, tasks, B_BUDGET

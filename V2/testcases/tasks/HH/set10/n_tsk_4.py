"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.996228, 'e_o_k': [0.774844, 0.619875], 'p_i': 10, 'u_i': 2.6429},
        {'id': 1, 'e_m': 1.043537, 'e_o_k': [0.434600, 0.347680, 0.278144, 0.222515, 0.178012], 'p_i': 20, 'u_i': 1.6574},
        {'id': 2, 'e_m': 19.524281, 'e_o_k': [8.131245, 6.504996, 5.203997, 4.163197, 3.330558], 'p_i': 40, 'u_i': 4.4970},
        {'id': 3, 'e_m': 12.807466, 'e_o_k': [7.348546, 5.878837, 4.703069], 'p_i': 80, 'u_i': 1.4275},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET

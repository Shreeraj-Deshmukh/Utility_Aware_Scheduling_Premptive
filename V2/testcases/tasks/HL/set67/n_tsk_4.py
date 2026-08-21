"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1067, "set": 67, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.012700, 'e_o_k': [0.207521, 0.166016, 0.132813], 'p_i': 10, 'u_i': 4.3936},
        {'id': 1, 'e_m': 6.068499, 'e_o_k': [1.243545, 0.994836, 0.795869], 'p_i': 20, 'u_i': 2.8467},
        {'id': 2, 'e_m': 8.216760, 'e_o_k': [1.391728, 1.113382, 0.890706, 0.712565], 'p_i': 40, 'u_i': 2.7697},
        {'id': 3, 'e_m': 15.190882, 'e_o_k': [2.058787, 1.647029, 1.317624, 1.054099, 0.843279, 0.674623], 'p_i': 80, 'u_i': 2.4720},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET

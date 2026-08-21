"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.617973, 'e_o_k': [0.234507, 0.187606, 0.150085, 0.120068, 0.096054, 0.076843], 'p_i': 10, 'u_i': 3.2393},
        {'id': 1, 'e_m': 1.095309, 'e_o_k': [0.415645, 0.332516, 0.266013, 0.212810, 0.170248, 0.136199], 'p_i': 20, 'u_i': 4.1852},
        {'id': 2, 'e_m': 5.386398, 'e_o_k': [2.554525, 2.043620, 1.634896, 1.307917], 'p_i': 40, 'u_i': 4.0538},
        {'id': 3, 'e_m': 11.902184, 'e_o_k': [5.644667, 4.515734, 3.612587, 2.890070], 'p_i': 80, 'u_i': 4.3622},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET

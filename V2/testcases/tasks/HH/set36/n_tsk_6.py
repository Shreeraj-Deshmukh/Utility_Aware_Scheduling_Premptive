"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.287406, 'e_o_k': [0.738675, 0.590940, 0.472752], 'p_i': 10, 'u_i': 1.0054},
        {'id': 1, 'e_m': 1.012025, 'e_o_k': [0.479957, 0.383966, 0.307173, 0.245738], 'p_i': 20, 'u_i': 3.4815},
        {'id': 2, 'e_m': 1.154572, 'e_o_k': [0.898000, 0.718400], 'p_i': 40, 'u_i': 3.3828},
        {'id': 3, 'e_m': 7.183412, 'e_o_k': [3.406767, 2.725414, 2.180331, 1.744265], 'p_i': 80, 'u_i': 4.2011},
        {'id': 4, 'e_m': 19.309471, 'e_o_k': [9.157608, 7.326087, 5.860869, 4.688695], 'p_i': 40, 'u_i': 4.7650},
        {'id': 5, 'e_m': 1.541158, 'e_o_k': [0.884271, 0.707417, 0.565934], 'p_i': 80, 'u_i': 4.1252},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET

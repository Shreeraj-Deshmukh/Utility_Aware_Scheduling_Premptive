"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.428398, 'e_o_k': [0.203170, 0.162536, 0.130029, 0.104023], 'p_i': 10, 'u_i': 3.5166},
        {'id': 1, 'e_m': 6.657356, 'e_o_k': [3.157283, 2.525826, 2.020661, 1.616529], 'p_i': 20, 'u_i': 2.8575},
        {'id': 2, 'e_m': 16.190522, 'e_o_k': [6.742840, 5.394272, 4.315418, 3.452334, 2.761867], 'p_i': 40, 'u_i': 2.8209},
        {'id': 3, 'e_m': 1.562346, 'e_o_k': [1.215158, 0.972127], 'p_i': 80, 'u_i': 2.9332},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET

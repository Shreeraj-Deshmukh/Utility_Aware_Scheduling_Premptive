"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1031, "set": 31, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.428398, 'e_o_k': [0.072561, 0.058049, 0.046439, 0.037151], 'p_i': 10, 'u_i': 3.5166},
        {'id': 1, 'e_m': 6.657356, 'e_o_k': [1.127601, 0.902081, 0.721665, 0.577332], 'p_i': 20, 'u_i': 2.8575},
        {'id': 2, 'e_m': 16.190522, 'e_o_k': [2.408157, 1.926526, 1.541221, 1.232976, 0.986381], 'p_i': 40, 'u_i': 2.8209},
        {'id': 3, 'e_m': 1.562346, 'e_o_k': [0.433985, 0.347188], 'p_i': 80, 'u_i': 2.9332},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET

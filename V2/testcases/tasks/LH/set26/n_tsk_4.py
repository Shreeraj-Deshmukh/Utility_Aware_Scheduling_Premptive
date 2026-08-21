"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.821433, 'e_o_k': [1.338078, 1.070462, 0.856370, 0.685096], 'p_i': 10, 'u_i': 1.8833},
        {'id': 1, 'e_m': 0.734372, 'e_o_k': [0.305843, 0.244674, 0.195739, 0.156591, 0.125273], 'p_i': 20, 'u_i': 2.8074},
        {'id': 2, 'e_m': 1.986615, 'e_o_k': [0.753876, 0.603101, 0.482481, 0.385985, 0.308788, 0.247030], 'p_i': 40, 'u_i': 2.2803},
        {'id': 3, 'e_m': 2.517821, 'e_o_k': [0.955457, 0.764366, 0.611493, 0.489194, 0.391355, 0.313084], 'p_i': 80, 'u_i': 3.9685},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET

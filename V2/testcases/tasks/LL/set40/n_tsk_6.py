"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199966, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199966, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.846222, 'e_o_k': [0.143330, 0.114664, 0.091731, 0.073385], 'p_i': 10, 'u_i': 3.4352},
        {'id': 1, 'e_m': 0.836504, 'e_o_k': [0.141684, 0.113347, 0.090678, 0.072542], 'p_i': 20, 'u_i': 3.4020},
        {'id': 2, 'e_m': 4.190220, 'e_o_k': [0.858652, 0.686921, 0.549537], 'p_i': 40, 'u_i': 3.4221},
        {'id': 3, 'e_m': 5.291011, 'e_o_k': [0.786978, 0.629582, 0.503666, 0.402933, 0.322346], 'p_i': 80, 'u_i': 3.9841},
        {'id': 4, 'e_m': 0.605237, 'e_o_k': [0.124024, 0.099219, 0.079375], 'p_i': 40, 'u_i': 2.4868},
        {'id': 5, 'e_m': 0.875285, 'e_o_k': [0.118625, 0.094900, 0.075920, 0.060736, 0.048589, 0.038871], 'p_i': 10, 'u_i': 2.1829},
    ]
    B_BUDGET = 55.199966
    return processors, tasks, B_BUDGET

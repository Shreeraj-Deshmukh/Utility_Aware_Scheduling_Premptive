"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320008, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1040, "set": 40, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.308392, 'e_o_k': [0.620511, 0.496409, 0.397127, 0.317702], 'p_i': 10, 'u_i': 4.9199},
        {'id': 1, 'e_m': 1.333159, 'e_o_k': [0.632257, 0.505805, 0.404644, 0.323715], 'p_i': 20, 'u_i': 1.0213},
        {'id': 2, 'e_m': 6.197007, 'e_o_k': [2.938960, 2.351168, 1.880934, 1.504748], 'p_i': 40, 'u_i': 3.4352},
        {'id': 3, 'e_m': 3.806219, 'e_o_k': [1.805117, 1.444094, 1.155275, 0.924220], 'p_i': 80, 'u_i': 3.4020},
    ]
    B_BUDGET = 88.320008
    return processors, tasks, B_BUDGET

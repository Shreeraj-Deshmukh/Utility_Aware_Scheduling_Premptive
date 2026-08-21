"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.320007, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1087, "set": 87, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.661504, 'e_o_k': [0.787976, 0.630381, 0.504305, 0.403444], 'p_i': 10, 'u_i': 4.1671},
        {'id': 1, 'e_m': 0.341465, 'e_o_k': [0.195923, 0.156738, 0.125390], 'p_i': 20, 'u_i': 4.3098},
        {'id': 2, 'e_m': 1.861171, 'e_o_k': [0.882669, 0.706135, 0.564908, 0.451927], 'p_i': 40, 'u_i': 1.7953},
        {'id': 3, 'e_m': 13.619767, 'e_o_k': [5.168400, 4.134720, 3.307776, 2.646221, 2.116977, 1.693581], 'p_i': 80, 'u_i': 2.0773},
    ]
    B_BUDGET = 88.320007
    return processors, tasks, B_BUDGET

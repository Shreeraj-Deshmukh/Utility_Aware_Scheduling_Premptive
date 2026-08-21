"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.926251, 'e_o_k': [0.385754, 0.308603, 0.246883, 0.197506, 0.158005], 'p_i': 10, 'u_i': 2.6037},
        {'id': 1, 'e_m': 2.259146, 'e_o_k': [1.757114, 1.405691], 'p_i': 20, 'u_i': 2.6419},
        {'id': 2, 'e_m': 0.063566, 'e_o_k': [0.026473, 0.021178, 0.016943, 0.013554, 0.010843], 'p_i': 40, 'u_i': 1.5138},
        {'id': 3, 'e_m': 2.910747, 'e_o_k': [1.670101, 1.336081, 1.068864], 'p_i': 80, 'u_i': 4.9479},
        {'id': 4, 'e_m': 8.790372, 'e_o_k': [5.043656, 4.034925, 3.227940], 'p_i': 80, 'u_i': 2.1346},
        {'id': 5, 'e_m': 0.465645, 'e_o_k': [0.362168, 0.289735], 'p_i': 10, 'u_i': 1.3827},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET

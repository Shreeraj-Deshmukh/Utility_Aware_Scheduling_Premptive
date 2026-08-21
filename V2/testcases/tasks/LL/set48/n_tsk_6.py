"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.926251, 'e_o_k': [0.137769, 0.110215, 0.088172, 0.070538, 0.056430], 'p_i': 10, 'u_i': 2.6037},
        {'id': 1, 'e_m': 2.259146, 'e_o_k': [0.627541, 0.502033], 'p_i': 20, 'u_i': 2.6419},
        {'id': 2, 'e_m': 0.063566, 'e_o_k': [0.009455, 0.007564, 0.006051, 0.004841, 0.003873], 'p_i': 40, 'u_i': 1.5138},
        {'id': 3, 'e_m': 2.910747, 'e_o_k': [0.596465, 0.477172, 0.381737], 'p_i': 80, 'u_i': 4.9479},
        {'id': 4, 'e_m': 8.790372, 'e_o_k': [1.801306, 1.441045, 1.152836], 'p_i': 80, 'u_i': 2.1346},
        {'id': 5, 'e_m': 0.465645, 'e_o_k': [0.129346, 0.103477], 'p_i': 10, 'u_i': 1.3827},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET

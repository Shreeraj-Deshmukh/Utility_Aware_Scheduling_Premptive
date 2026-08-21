"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.639995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1043, "set": 43, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.119976, 'e_o_k': [0.068839, 0.055071, 0.044057], 'p_i': 10, 'u_i': 4.5752},
        {'id': 1, 'e_m': 6.256174, 'e_o_k': [2.967020, 2.373616, 1.898893, 1.519114], 'p_i': 20, 'u_i': 3.6570},
        {'id': 2, 'e_m': 10.041186, 'e_o_k': [4.762080, 3.809664, 3.047731, 2.438185], 'p_i': 40, 'u_i': 3.9951},
        {'id': 3, 'e_m': 17.933122, 'e_o_k': [10.289496, 8.231597, 6.585277], 'p_i': 80, 'u_i': 2.8657},
    ]
    B_BUDGET = 176.639995
    return processors, tasks, B_BUDGET

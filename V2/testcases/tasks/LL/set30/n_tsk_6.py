"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199985, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199985, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.034273, 'e_o_k': [0.009520, 0.007616], 'p_i': 10, 'u_i': 2.7951},
        {'id': 1, 'e_m': 1.524612, 'e_o_k': [0.312420, 0.249936, 0.199949], 'p_i': 20, 'u_i': 4.2173},
        {'id': 2, 'e_m': 2.019286, 'e_o_k': [0.560913, 0.448730], 'p_i': 40, 'u_i': 4.5788},
        {'id': 3, 'e_m': 4.113880, 'e_o_k': [0.843008, 0.674407, 0.539525], 'p_i': 80, 'u_i': 1.6533},
        {'id': 4, 'e_m': 14.178554, 'e_o_k': [2.401517, 1.921213, 1.536971, 1.229576], 'p_i': 80, 'u_i': 4.3793},
        {'id': 5, 'e_m': 3.296359, 'e_o_k': [0.558326, 0.446661, 0.357329, 0.285863], 'p_i': 80, 'u_i': 2.7000},
    ]
    B_BUDGET = 55.199985
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.034273, 'e_o_k': [0.026657, 0.021326], 'p_i': 10, 'u_i': 2.7951},
        {'id': 1, 'e_m': 1.524612, 'e_o_k': [0.874777, 0.699822, 0.559857], 'p_i': 20, 'u_i': 4.2173},
        {'id': 2, 'e_m': 2.019286, 'e_o_k': [1.570556, 1.256445], 'p_i': 40, 'u_i': 4.5788},
        {'id': 3, 'e_m': 4.113880, 'e_o_k': [2.360423, 1.888339, 1.510671], 'p_i': 80, 'u_i': 1.6533},
        {'id': 4, 'e_m': 14.178554, 'e_o_k': [6.724246, 5.379397, 4.303518, 3.442814], 'p_i': 80, 'u_i': 4.3793},
        {'id': 5, 'e_m': 3.296359, 'e_o_k': [1.563314, 1.250651, 1.000521, 0.800417], 'p_i': 80, 'u_i': 2.7000},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET

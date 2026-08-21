"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.20001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.20001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1004, "set": 4, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.001779, 'e_o_k': [0.135769, 0.108615, 0.086892, 0.069514, 0.055611, 0.044489], 'p_i': 10, 'u_i': 3.5500},
        {'id': 1, 'e_m': 0.072069, 'e_o_k': [0.014768, 0.011815, 0.009452], 'p_i': 20, 'u_i': 2.3662},
        {'id': 2, 'e_m': 4.582147, 'e_o_k': [1.272819, 1.018255], 'p_i': 40, 'u_i': 3.8013},
        {'id': 3, 'e_m': 14.533199, 'e_o_k': [2.978115, 2.382492, 1.905993], 'p_i': 80, 'u_i': 4.3808},
    ]
    B_BUDGET = 55.200010
    return processors, tasks, B_BUDGET

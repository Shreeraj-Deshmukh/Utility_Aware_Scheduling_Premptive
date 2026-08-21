"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1057, "set": 57, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.201488, 'e_o_k': [0.115608, 0.092486, 0.073989], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.441830, 'e_o_k': [0.827279, 0.661823, 0.529459], 'p_i': 20, 'u_i': 1.1969},
        {'id': 2, 'e_m': 8.661890, 'e_o_k': [4.969937, 3.975950, 3.180760], 'p_i': 40, 'u_i': 4.6056},
        {'id': 3, 'e_m': 8.902172, 'e_o_k': [5.107804, 4.086243, 3.268994], 'p_i': 80, 'u_i': 2.0280},
        {'id': 4, 'e_m': 5.993625, 'e_o_k': [3.438965, 2.751172, 2.200938], 'p_i': 40, 'u_i': 3.8591},
        {'id': 5, 'e_m': 4.342413, 'e_o_k': [2.491548, 1.993239, 1.594591], 'p_i': 80, 'u_i': 4.1547},
        {'id': 6, 'e_m': 1.301354, 'e_o_k': [0.746678, 0.597343, 0.477874], 'p_i': 10, 'u_i': 4.9057},
        {'id': 7, 'e_m': 3.654332, 'e_o_k': [2.096748, 1.677398, 1.341919], 'p_i': 80, 'u_i': 4.2009},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET

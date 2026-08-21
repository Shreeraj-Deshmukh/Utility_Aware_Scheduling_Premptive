"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.122529, 'e_o_k': [0.046497, 0.037198, 0.029758, 0.023806, 0.019045, 0.015236], 'p_i': 10, 'u_i': 4.9047},
        {'id': 1, 'e_m': 0.419662, 'e_o_k': [0.240790, 0.192632, 0.154105], 'p_i': 20, 'u_i': 3.2321},
        {'id': 2, 'e_m': 2.339399, 'e_o_k': [0.974285, 0.779428, 0.623543, 0.498834, 0.399067], 'p_i': 40, 'u_i': 3.3144},
        {'id': 3, 'e_m': 1.435058, 'e_o_k': [0.544573, 0.435658, 0.348527, 0.278821, 0.223057, 0.178446], 'p_i': 80, 'u_i': 1.1307},
        {'id': 4, 'e_m': 1.500724, 'e_o_k': [0.625004, 0.500003, 0.400003, 0.320002, 0.256002], 'p_i': 20, 'u_i': 4.3260},
        {'id': 5, 'e_m': 4.306093, 'e_o_k': [2.470709, 1.976567, 1.581254], 'p_i': 20, 'u_i': 4.7000},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET

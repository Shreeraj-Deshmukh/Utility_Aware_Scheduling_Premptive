"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640014, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640014, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1074, "set": 74, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.330892, 'e_o_k': [0.137806, 0.110245, 0.088196, 0.070557, 0.056445], 'p_i': 10, 'u_i': 3.5312},
        {'id': 1, 'e_m': 3.283430, 'e_o_k': [1.245989, 0.996791, 0.797433, 0.637946, 0.510357, 0.408286], 'p_i': 20, 'u_i': 1.4207},
        {'id': 2, 'e_m': 10.363895, 'e_o_k': [4.316234, 3.452987, 2.762390, 2.209912, 1.767930], 'p_i': 40, 'u_i': 4.1417},
        {'id': 3, 'e_m': 21.476872, 'e_o_k': [8.944437, 7.155550, 5.724440, 4.579552, 3.663641], 'p_i': 80, 'u_i': 4.9795},
        {'id': 4, 'e_m': 0.405589, 'e_o_k': [0.232715, 0.186172, 0.148938], 'p_i': 20, 'u_i': 4.9448},
        {'id': 5, 'e_m': 0.549016, 'e_o_k': [0.228648, 0.182918, 0.146335, 0.117068, 0.093654], 'p_i': 10, 'u_i': 4.4554},
    ]
    B_BUDGET = 176.640014
    return processors, tasks, B_BUDGET

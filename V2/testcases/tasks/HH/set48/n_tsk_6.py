"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640006, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640006, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.852501, 'e_o_k': [0.771508, 0.617207, 0.493765, 0.395012, 0.316010], 'p_i': 10, 'u_i': 2.6037},
        {'id': 1, 'e_m': 4.518293, 'e_o_k': [3.514228, 2.811382], 'p_i': 20, 'u_i': 2.6419},
        {'id': 2, 'e_m': 0.127131, 'e_o_k': [0.052946, 0.042357, 0.033886, 0.027108, 0.021687], 'p_i': 40, 'u_i': 1.5138},
        {'id': 3, 'e_m': 5.821494, 'e_o_k': [3.340201, 2.672161, 2.137729], 'p_i': 80, 'u_i': 4.9479},
        {'id': 4, 'e_m': 17.580744, 'e_o_k': [10.087312, 8.069850, 6.455880], 'p_i': 80, 'u_i': 2.1346},
        {'id': 5, 'e_m': 0.931290, 'e_o_k': [0.724337, 0.579469], 'p_i': 10, 'u_i': 1.3827},
    ]
    B_BUDGET = 176.640006
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 114.816009, "H": 80, "J": 27, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.4, "seed": 1057, "set": 57, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 114.816009, "H": 80, "J": 27, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.4, "seed": 1057, "set": 57, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.201488, 'e_o_k': [0.083913, 0.067131, 0.053705, 0.042964, 0.034371], 'p_i': 10, 'u_i': 4.1139},
        {'id': 1, 'e_m': 1.441830, 'e_o_k': [0.547142, 0.437714, 0.350171, 0.280137, 0.224110, 0.179288], 'p_i': 20, 'u_i': 3.3967},
        {'id': 2, 'e_m': 8.661890, 'e_o_k': [6.737026, 5.389621], 'p_i': 40, 'u_i': 1.9449},
        {'id': 3, 'e_m': 8.902172, 'e_o_k': [6.923912, 5.539130], 'p_i': 80, 'u_i': 4.6056},
        {'id': 4, 'e_m': 5.993625, 'e_o_k': [4.661709, 3.729367], 'p_i': 40, 'u_i': 2.0280},
        {'id': 5, 'e_m': 4.342413, 'e_o_k': [1.647849, 1.318280, 1.054624, 0.843699, 0.674959, 0.539967], 'p_i': 80, 'u_i': 1.2717},
        {'id': 6, 'e_m': 1.301354, 'e_o_k': [1.012164, 0.809731], 'p_i': 10, 'u_i': 1.1584},
        {'id': 7, 'e_m': 3.654332, 'e_o_k': [2.096748, 1.677398, 1.341919], 'p_i': 80, 'u_i': 3.8897},
    ]
    B_BUDGET = 114.816009
    return processors, tasks, B_BUDGET

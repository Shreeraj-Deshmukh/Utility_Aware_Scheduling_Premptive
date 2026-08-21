"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280009, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280009, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.238680, 'e_o_k': [0.329134, 0.263307, 0.210646, 0.168517], 'p_i': 10, 'u_i': 4.7284},
        {'id': 1, 'e_m': 1.103119, 'e_o_k': [0.183853, 0.147083], 'p_i': 20, 'u_i': 2.9850},
        {'id': 2, 'e_m': 15.020217, 'e_o_k': [2.503370, 2.002696], 'p_i': 40, 'u_i': 4.6281},
        {'id': 3, 'e_m': 14.299293, 'e_o_k': [1.276115, 1.020892, 0.816714, 0.653371, 0.522697], 'p_i': 80, 'u_i': 1.0041},
        {'id': 4, 'e_m': 10.314007, 'e_o_k': [0.920455, 0.736364, 0.589091, 0.471273, 0.377018], 'p_i': 40, 'u_i': 2.2799},
        {'id': 5, 'e_m': 0.633103, 'e_o_k': [0.064340, 0.051472, 0.041177, 0.032942], 'p_i': 10, 'u_i': 4.7563},
        {'id': 6, 'e_m': 1.380848, 'e_o_k': [0.230141, 0.184113], 'p_i': 10, 'u_i': 4.7914},
        {'id': 7, 'e_m': 32.598741, 'e_o_k': [2.909217, 2.327373, 1.861899, 1.489519, 1.191615], 'p_i': 80, 'u_i': 4.0401},
    ]
    B_BUDGET = 215.280009
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359998, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359998, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.668474, 'e_o_k': [0.278079, 0.222463], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 4.125898, 'e_o_k': [0.507283, 0.405826, 0.324661], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 4.338557, 'e_o_k': [0.723093, 0.578474], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 26.053971, 'e_o_k': [2.647761, 2.118209, 1.694567, 1.355654], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.563012, 'e_o_k': [0.093835, 0.075068], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 2.423436, 'e_o_k': [0.246284, 0.197027, 0.157622, 0.126097], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 2.369895, 'e_o_k': [0.291381, 0.233104, 0.186484], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 2.852355, 'e_o_k': [0.350699, 0.280559, 0.224448], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 191.359998
    return processors, tasks, B_BUDGET

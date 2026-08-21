"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.280013, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.280013, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.877033, 'e_o_k': [0.312839, 0.250271], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 4.641636, 'e_o_k': [0.570693, 0.456554, 0.365243], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 4.880877, 'e_o_k': [0.813479, 0.650784], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 29.310717, 'e_o_k': [2.978731, 2.382985, 1.906388, 1.525110], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.633389, 'e_o_k': [0.105565, 0.084452], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 2.726365, 'e_o_k': [0.277070, 0.221656, 0.177325, 0.141860], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 2.666132, 'e_o_k': [0.327803, 0.262242, 0.209794], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 3.208899, 'e_o_k': [0.394537, 0.315629, 0.252504], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 215.280013
    return processors, tasks, B_BUDGET

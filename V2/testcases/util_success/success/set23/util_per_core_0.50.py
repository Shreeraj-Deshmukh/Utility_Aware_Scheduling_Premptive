"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600001, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600001, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.334905, 'e_o_k': [0.034035, 0.027228, 0.021782, 0.017426], 'p_i': 10, 'u_i': 2.0521},
        {'id': 1, 'e_m': 2.970430, 'e_o_k': [0.265091, 0.212073, 0.169658, 0.135726, 0.108581], 'p_i': 20, 'u_i': 4.1261},
        {'id': 2, 'e_m': 5.280163, 'e_o_k': [0.536602, 0.429282, 0.343425, 0.274740], 'p_i': 40, 'u_i': 2.8820},
        {'id': 3, 'e_m': 27.032711, 'e_o_k': [2.198210, 1.758568, 1.406855, 1.125484, 0.900387, 0.720310], 'p_i': 80, 'u_i': 1.8301},
        {'id': 4, 'e_m': 0.006176, 'e_o_k': [0.001029, 0.000823], 'p_i': 20, 'u_i': 2.8656},
        {'id': 5, 'e_m': 3.364774, 'e_o_k': [0.273612, 0.218890, 0.175112, 0.140089, 0.112072, 0.089657], 'p_i': 20, 'u_i': 4.7863},
        {'id': 6, 'e_m': 0.166709, 'e_o_k': [0.013556, 0.010845, 0.008676, 0.006941, 0.005553, 0.004442], 'p_i': 20, 'u_i': 3.1132},
        {'id': 7, 'e_m': 1.711921, 'e_o_k': [0.173976, 0.139181, 0.111344, 0.089076], 'p_i': 10, 'u_i': 2.8421},
    ]
    B_BUDGET = 119.600001
    return processors, tasks, B_BUDGET

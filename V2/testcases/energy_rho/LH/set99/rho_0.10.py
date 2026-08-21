"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 41.951996, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.1, "seed": 1099, "set": 99, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}
"""

_SPEC = '{"B": 41.951996, "H": 80, "J": 28, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.1, "seed": 1099, "set": 99, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.485314, 'e_o_k': [0.202118, 0.161694, 0.129356, 0.103484, 0.082788], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 1.461505, 'e_o_k': [0.608671, 0.486937, 0.389549, 0.311639, 0.249312], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 0.554952, 'e_o_k': [0.263189, 0.210551, 0.168441, 0.134753], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 1.824306, 'e_o_k': [1.046733, 0.837386, 0.669909], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 0.517558, 'e_o_k': [0.296959, 0.237568, 0.190054], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 5.062609, 'e_o_k': [2.108417, 1.686733, 1.349387, 1.079509, 0.863607], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 2.445941, 'e_o_k': [1.403409, 1.122727, 0.898182], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.179690, 'e_o_k': [0.139759, 0.111807], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 41.951996
    return processors, tasks, B_BUDGET

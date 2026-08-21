"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759998, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759998, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.761462, 'e_o_k': [0.067955, 0.054364, 0.043491, 0.034793, 0.027835], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 1.003603, 'e_o_k': [0.081610, 0.065288, 0.052230, 0.041784, 0.033427, 0.026742], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 0.911527, 'e_o_k': [0.074122, 0.059298, 0.047438, 0.037951, 0.030361, 0.024288], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 8.570605, 'e_o_k': [1.428434, 1.142747], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 3.144563, 'e_o_k': [0.319569, 0.255656, 0.204524, 0.163620], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.405786, 'e_o_k': [0.041238, 0.032991, 0.026393, 0.021114], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 4.245526, 'e_o_k': [0.707588, 0.566070], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.491358, 'e_o_k': [0.081893, 0.065514], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 71.759998
    return processors, tasks, B_BUDGET

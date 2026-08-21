"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519997, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519997, "H": 80, "J": 43, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.251355, 'e_o_k': [0.208559, 0.166847], 'p_i': 10, 'u_i': 4.4926},
        {'id': 1, 'e_m': 3.094424, 'e_o_k': [0.380462, 0.304370, 0.243496], 'p_i': 20, 'u_i': 3.2922},
        {'id': 2, 'e_m': 3.253918, 'e_o_k': [0.542320, 0.433856], 'p_i': 40, 'u_i': 3.7450},
        {'id': 3, 'e_m': 19.540478, 'e_o_k': [1.985821, 1.588657, 1.270925, 1.016740], 'p_i': 80, 'u_i': 4.8771},
        {'id': 4, 'e_m': 0.422259, 'e_o_k': [0.070377, 0.056301], 'p_i': 20, 'u_i': 4.0203},
        {'id': 5, 'e_m': 1.817577, 'e_o_k': [0.184713, 0.147770, 0.118216, 0.094573], 'p_i': 10, 'u_i': 3.4418},
        {'id': 6, 'e_m': 1.777421, 'e_o_k': [0.218535, 0.174828, 0.139863], 'p_i': 10, 'u_i': 4.8003},
        {'id': 7, 'e_m': 2.139266, 'e_o_k': [0.263025, 0.210420, 0.168336], 'p_i': 10, 'u_i': 3.9154},
    ]
    B_BUDGET = 143.519997
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520007, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.642253, 'e_o_k': [0.166896, 0.133517, 0.106813, 0.085451], 'p_i': 10, 'u_i': 4.0093},
        {'id': 1, 'e_m': 9.023041, 'e_o_k': [1.109390, 0.887512, 0.710010], 'p_i': 20, 'u_i': 1.1110},
        {'id': 2, 'e_m': 2.047289, 'e_o_k': [0.166479, 0.133183, 0.106546, 0.085237, 0.068190, 0.054552], 'p_i': 40, 'u_i': 1.1701},
        {'id': 3, 'e_m': 1.813946, 'e_o_k': [0.223026, 0.178421, 0.142737], 'p_i': 80, 'u_i': 4.4848},
        {'id': 4, 'e_m': 3.747313, 'e_o_k': [0.380824, 0.304660, 0.243728, 0.194982], 'p_i': 20, 'u_i': 3.6888},
        {'id': 5, 'e_m': 1.334558, 'e_o_k': [0.164085, 0.131268, 0.105014], 'p_i': 20, 'u_i': 2.1778},
        {'id': 6, 'e_m': 0.565343, 'e_o_k': [0.094224, 0.075379], 'p_i': 10, 'u_i': 3.8298},
        {'id': 7, 'e_m': 8.005529, 'e_o_k': [1.334255, 1.067404], 'p_i': 40, 'u_i': 2.6902},
    ]
    B_BUDGET = 143.520007
    return processors, tasks, B_BUDGET

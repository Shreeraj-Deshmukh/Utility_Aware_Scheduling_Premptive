"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.119998, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.119998, "H": 80, "J": 20, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1059, "set": 59, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.258683, 'e_o_k': [0.400658, 0.320526, 0.256421], 'p_i': 10, 'u_i': 3.5538},
        {'id': 1, 'e_m': 6.003729, 'e_o_k': [0.738163, 0.590531, 0.472425], 'p_i': 20, 'u_i': 3.5798},
        {'id': 2, 'e_m': 1.271302, 'e_o_k': [0.113455, 0.090764, 0.072611, 0.058089, 0.046471], 'p_i': 40, 'u_i': 4.6121},
        {'id': 3, 'e_m': 9.711360, 'e_o_k': [1.194020, 0.955216, 0.764173], 'p_i': 80, 'u_i': 1.8652},
        {'id': 4, 'e_m': 34.149509, 'e_o_k': [3.470479, 2.776383, 2.221106, 1.776885], 'p_i': 80, 'u_i': 3.7246},
        {'id': 5, 'e_m': 26.293954, 'e_o_k': [2.346557, 1.877246, 1.501797, 1.201437, 0.961150], 'p_i': 80, 'u_i': 2.8258},
        {'id': 6, 'e_m': 36.697511, 'e_o_k': [2.984120, 2.387296, 1.909837, 1.527869, 1.222295, 0.977836], 'p_i': 80, 'u_i': 3.9534},
        {'id': 7, 'e_m': 8.260339, 'e_o_k': [1.376723, 1.101379], 'p_i': 40, 'u_i': 4.8137},
    ]
    B_BUDGET = 263.119998
    return processors, tasks, B_BUDGET

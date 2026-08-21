"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 32, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.355801, 'e_o_k': [0.098834, 0.079067], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 0.978019, 'e_o_k': [0.271672, 0.217338], 'p_i': 20, 'u_i': 4.0273},
        {'id': 2, 'e_m': 3.289454, 'e_o_k': [0.913737, 0.730990], 'p_i': 40, 'u_i': 2.2476},
        {'id': 3, 'e_m': 7.449156, 'e_o_k': [2.069210, 1.655368], 'p_i': 80, 'u_i': 1.3199},
        {'id': 4, 'e_m': 2.409551, 'e_o_k': [0.669320, 0.535456], 'p_i': 80, 'u_i': 3.4892},
        {'id': 5, 'e_m': 0.229718, 'e_o_k': [0.063811, 0.051048], 'p_i': 10, 'u_i': 1.4050},
        {'id': 6, 'e_m': 0.659831, 'e_o_k': [0.183286, 0.146629], 'p_i': 20, 'u_i': 3.5798},
        {'id': 7, 'e_m': 1.081708, 'e_o_k': [0.300474, 0.240380], 'p_i': 20, 'u_i': 2.2529},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET

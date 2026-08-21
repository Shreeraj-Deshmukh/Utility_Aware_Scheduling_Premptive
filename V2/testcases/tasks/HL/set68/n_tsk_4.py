"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400013, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.005293, 'e_o_k': [0.339650, 0.271720, 0.217376, 0.173901], 'p_i': 10, 'u_i': 2.8933},
        {'id': 1, 'e_m': 6.534487, 'e_o_k': [0.885605, 0.708484, 0.566787, 0.453430, 0.362744, 0.290195], 'p_i': 20, 'u_i': 4.7664},
        {'id': 2, 'e_m': 5.399596, 'e_o_k': [1.106475, 0.885180, 0.708144], 'p_i': 40, 'u_i': 2.0608},
        {'id': 3, 'e_m': 11.020515, 'e_o_k': [1.639177, 1.311342, 1.049073, 0.839259, 0.671407], 'p_i': 80, 'u_i': 4.9277},
    ]
    B_BUDGET = 110.400013
    return processors, tasks, B_BUDGET

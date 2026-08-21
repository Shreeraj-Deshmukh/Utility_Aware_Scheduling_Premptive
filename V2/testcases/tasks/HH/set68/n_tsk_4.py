"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.64, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.005293, 'e_o_k': [0.951020, 0.760816, 0.608653, 0.486922], 'p_i': 10, 'u_i': 2.8933},
        {'id': 1, 'e_m': 6.534487, 'e_o_k': [2.479693, 1.983754, 1.587003, 1.269603, 1.015682, 0.812546], 'p_i': 20, 'u_i': 4.7664},
        {'id': 2, 'e_m': 5.399596, 'e_o_k': [3.098129, 2.478503, 1.982802], 'p_i': 40, 'u_i': 2.0608},
        {'id': 3, 'e_m': 11.020515, 'e_o_k': [4.589696, 3.671757, 2.937405, 2.349924, 1.879939], 'p_i': 80, 'u_i': 4.9277},
    ]
    B_BUDGET = 176.640000
    return processors, tasks, B_BUDGET

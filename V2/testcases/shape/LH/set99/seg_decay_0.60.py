"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319983, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319983, "H": 80, "J": 28, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1099, "set": 99, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.485314, 'e_o_k': [0.294691, 0.176815, 0.106089, 0.063653, 0.038192], 'p_i': 10, 'u_i': 1.8657},
        {'id': 1, 'e_m': 1.461505, 'e_o_k': [0.887451, 0.532471, 0.319482, 0.191689, 0.115014], 'p_i': 20, 'u_i': 1.6547},
        {'id': 2, 'e_m': 0.554952, 'e_o_k': [0.357046, 0.214228, 0.128537, 0.077122], 'p_i': 40, 'u_i': 3.2690},
        {'id': 3, 'e_m': 1.824306, 'e_o_k': [1.303076, 0.781846, 0.469107], 'p_i': 80, 'u_i': 2.0883},
        {'id': 4, 'e_m': 0.517558, 'e_o_k': [0.369684, 0.221810, 0.133086], 'p_i': 10, 'u_i': 2.4453},
        {'id': 5, 'e_m': 5.062609, 'e_o_k': [3.074104, 1.844462, 1.106677, 0.664006, 0.398404], 'p_i': 40, 'u_i': 4.4841},
        {'id': 6, 'e_m': 2.445941, 'e_o_k': [1.747101, 1.048260, 0.628956], 'p_i': 40, 'u_i': 2.2759},
        {'id': 7, 'e_m': 0.179690, 'e_o_k': [0.157229, 0.094337], 'p_i': 80, 'u_i': 4.2544},
    ]
    B_BUDGET = 88.319983
    return processors, tasks, B_BUDGET

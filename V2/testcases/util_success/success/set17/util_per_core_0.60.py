"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519999, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.190288, 'e_o_k': [0.096790, 0.077432, 0.061946, 0.049557, 0.039645, 0.031716], 'p_i': 10, 'u_i': 2.9192},
        {'id': 1, 'e_m': 1.574893, 'e_o_k': [0.160050, 0.128040, 0.102432, 0.081946], 'p_i': 20, 'u_i': 2.0454},
        {'id': 2, 'e_m': 11.306377, 'e_o_k': [0.919397, 0.735518, 0.588414, 0.470731, 0.376585, 0.301268], 'p_i': 40, 'u_i': 2.8602},
        {'id': 3, 'e_m': 25.683188, 'e_o_k': [4.280531, 3.424425], 'p_i': 80, 'u_i': 2.9521},
        {'id': 4, 'e_m': 1.281107, 'e_o_k': [0.213518, 0.170814], 'p_i': 10, 'u_i': 3.5497},
        {'id': 5, 'e_m': 4.968951, 'e_o_k': [0.504975, 0.403980, 0.323184, 0.258547], 'p_i': 40, 'u_i': 2.7971},
        {'id': 6, 'e_m': 2.758180, 'e_o_k': [0.224286, 0.179429, 0.143543, 0.114834, 0.091868, 0.073494], 'p_i': 80, 'u_i': 4.6429},
        {'id': 7, 'e_m': 8.937245, 'e_o_k': [1.489541, 1.191633], 'p_i': 80, 'u_i': 1.6248},
    ]
    B_BUDGET = 143.519999
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759998, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759998, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.379340, 'e_o_k': [0.063223, 0.050579], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.146414, 'e_o_k': [0.018002, 0.014401, 0.011521], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 7.638171, 'e_o_k': [1.273028, 1.018423], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 4.920884, 'e_o_k': [0.400150, 0.320120, 0.256096, 0.204877, 0.163901, 0.131121], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 3.404552, 'e_o_k': [0.567425, 0.453940], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 5.074118, 'e_o_k': [0.515662, 0.412530, 0.330024, 0.264019], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 0.813472, 'e_o_k': [0.072597, 0.058077, 0.046462, 0.037170, 0.029736], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.279523, 'e_o_k': [0.034368, 0.027494, 0.021995], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 71.759998
    return processors, tasks, B_BUDGET

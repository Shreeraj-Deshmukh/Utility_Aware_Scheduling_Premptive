"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200005, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200005, "H": 80, "J": 37, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.331086, 'e_o_k': [0.040707, 0.032566, 0.026053], 'p_i': 10, 'u_i': 3.6720},
        {'id': 1, 'e_m': 9.956911, 'e_o_k': [1.011881, 0.809505, 0.647604, 0.518083], 'p_i': 20, 'u_i': 3.1242},
        {'id': 2, 'e_m': 11.141940, 'e_o_k': [0.994343, 0.795474, 0.636379, 0.509103, 0.407283], 'p_i': 40, 'u_i': 4.4132},
        {'id': 3, 'e_m': 7.081277, 'e_o_k': [0.631956, 0.505565, 0.404452, 0.323561, 0.258849], 'p_i': 80, 'u_i': 1.8696},
        {'id': 4, 'e_m': 3.435165, 'e_o_k': [0.349102, 0.279282, 0.223425, 0.178740], 'p_i': 20, 'u_i': 4.5901},
        {'id': 5, 'e_m': 18.626903, 'e_o_k': [1.662325, 1.329860, 1.063888, 0.851110, 0.680888], 'p_i': 40, 'u_i': 2.7327},
        {'id': 6, 'e_m': 0.779876, 'e_o_k': [0.129979, 0.103983], 'p_i': 10, 'u_i': 2.2872},
        {'id': 7, 'e_m': 3.865631, 'e_o_k': [0.475282, 0.380226, 0.304181], 'p_i': 10, 'u_i': 3.8626},
    ]
    B_BUDGET = 239.200005
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640005, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640005, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.321452, 'e_o_k': [1.331981, 1.065585, 0.852468], 'p_i': 10, 'u_i': 2.0997},
        {'id': 1, 'e_m': 1.867881, 'e_o_k': [1.452797, 1.162237], 'p_i': 20, 'u_i': 1.8132},
        {'id': 2, 'e_m': 10.883768, 'e_o_k': [4.130149, 3.304119, 2.643295, 2.114636, 1.691709, 1.353367], 'p_i': 40, 'u_i': 1.3118},
        {'id': 3, 'e_m': 4.486259, 'e_o_k': [1.868385, 1.494708, 1.195766, 0.956613, 0.765291], 'p_i': 80, 'u_i': 1.6432},
        {'id': 4, 'e_m': 0.235105, 'e_o_k': [0.182859, 0.146287], 'p_i': 20, 'u_i': 3.2827},
        {'id': 5, 'e_m': 2.690661, 'e_o_k': [1.120575, 0.896460, 0.717168, 0.573734, 0.458988], 'p_i': 20, 'u_i': 1.0597},
    ]
    B_BUDGET = 176.640005
    return processors, tasks, B_BUDGET

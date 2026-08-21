"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.045412, 0.036330, 0.029064], 'p_i': 10, 'u_i': 2.5678},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.039451, 0.031560, 0.025248], 'p_i': 20, 'u_i': 3.0744},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [0.736368, 0.589094, 0.471276], 'p_i': 40, 'u_i': 3.1102},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [2.112778, 1.690222, 1.352178], 'p_i': 80, 'u_i': 3.9862},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.148723, 0.118979, 0.095183], 'p_i': 20, 'u_i': 1.5757},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.137941, 0.110352, 0.088282], 'p_i': 10, 'u_i': 4.9941},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.211879, 0.169503, 0.135602], 'p_i': 40, 'u_i': 1.7632},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.164294, 0.131435, 0.105148], 'p_i': 40, 'u_i': 1.4284},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET

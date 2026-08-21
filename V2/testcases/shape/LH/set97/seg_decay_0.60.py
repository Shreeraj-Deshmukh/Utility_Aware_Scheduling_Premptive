"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320009, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.320009, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.350656, 'e_o_k': [0.212925, 0.127755, 0.076653, 0.045992, 0.027595], 'p_i': 10, 'u_i': 4.4298},
        {'id': 1, 'e_m': 3.430445, 'e_o_k': [2.450318, 1.470191, 0.882114], 'p_i': 20, 'u_i': 1.5050},
        {'id': 2, 'e_m': 0.207300, 'e_o_k': [0.181387, 0.108832], 'p_i': 40, 'u_i': 2.3174},
        {'id': 3, 'e_m': 1.714842, 'e_o_k': [1.007308, 0.604385, 0.362631, 0.217579, 0.130547, 0.078328], 'p_i': 80, 'u_i': 4.0993},
        {'id': 4, 'e_m': 0.699429, 'e_o_k': [0.612000, 0.367200], 'p_i': 20, 'u_i': 2.5958},
        {'id': 5, 'e_m': 2.747339, 'e_o_k': [1.962385, 1.177431, 0.706459], 'p_i': 80, 'u_i': 1.3643},
        {'id': 6, 'e_m': 2.551296, 'e_o_k': [1.498647, 0.899188, 0.539513, 0.323708, 0.194225, 0.116535], 'p_i': 40, 'u_i': 1.6218},
        {'id': 7, 'e_m': 2.695881, 'e_o_k': [1.734483, 1.040690, 0.624414, 0.374648], 'p_i': 80, 'u_i': 1.2955},
    ]
    B_BUDGET = 88.320009
    return processors, tasks, B_BUDGET

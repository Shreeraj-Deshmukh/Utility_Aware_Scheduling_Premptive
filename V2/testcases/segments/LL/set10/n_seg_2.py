"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.061559, 0.049247], 'p_i': 10, 'u_i': 2.5678},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.053477, 0.042782], 'p_i': 20, 'u_i': 3.0744},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [0.998188, 0.798550], 'p_i': 40, 'u_i': 3.1102},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [2.863988, 2.291190], 'p_i': 80, 'u_i': 3.9862},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.201603, 0.161282], 'p_i': 20, 'u_i': 1.5757},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.186986, 0.149589], 'p_i': 10, 'u_i': 4.9941},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.287213, 0.229771], 'p_i': 40, 'u_i': 1.7632},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.222709, 0.178167], 'p_i': 40, 'u_i': 1.4284},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET

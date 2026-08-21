"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400002, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400002, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.261458, 'e_o_k': [0.905961, 0.724768], 'p_i': 10, 'u_i': 2.1780},
        {'id': 1, 'e_m': 1.108892, 'e_o_k': [0.308026, 0.246421], 'p_i': 20, 'u_i': 3.8388},
        {'id': 2, 'e_m': 2.887856, 'e_o_k': [0.802182, 0.641746], 'p_i': 40, 'u_i': 1.0041},
        {'id': 3, 'e_m': 7.831935, 'e_o_k': [2.175538, 1.740430], 'p_i': 80, 'u_i': 4.1994},
        {'id': 4, 'e_m': 1.667341, 'e_o_k': [0.463150, 0.370520], 'p_i': 40, 'u_i': 2.3676},
        {'id': 5, 'e_m': 0.734982, 'e_o_k': [0.204162, 0.163329], 'p_i': 10, 'u_i': 3.7622},
        {'id': 6, 'e_m': 0.370506, 'e_o_k': [0.102918, 0.082335], 'p_i': 10, 'u_i': 1.6504},
        {'id': 7, 'e_m': 7.686534, 'e_o_k': [2.135148, 1.708119], 'p_i': 80, 'u_i': 2.4020},
    ]
    B_BUDGET = 110.400002
    return processors, tasks, B_BUDGET

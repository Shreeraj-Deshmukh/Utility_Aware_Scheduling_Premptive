"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.456621, 'e_o_k': [0.298488, 0.238790, 0.191032], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 6.472983, 'e_o_k': [1.326431, 1.061145, 0.848916], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.070031, 'e_o_k': [0.219269, 0.175415, 0.140332], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 9.500976, 'e_o_k': [1.946921, 1.557537, 1.246030], 'p_i': 80, 'u_i': 4.1202},
        {'id': 4, 'e_m': 0.365435, 'e_o_k': [0.074884, 0.059907, 0.047926], 'p_i': 40, 'u_i': 4.7898},
        {'id': 5, 'e_m': 0.184044, 'e_o_k': [0.037714, 0.030171, 0.024137], 'p_i': 10, 'u_i': 3.8151},
        {'id': 6, 'e_m': 5.282667, 'e_o_k': [1.082514, 0.866011, 0.692809], 'p_i': 40, 'u_i': 2.4922},
        {'id': 7, 'e_m': 0.255688, 'e_o_k': [0.052395, 0.041916, 0.033533], 'p_i': 10, 'u_i': 1.4417},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET

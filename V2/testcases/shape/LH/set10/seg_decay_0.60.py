"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319993, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319993, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.130176, 0.078106, 0.046863, 0.028118, 0.016871, 0.010122], 'p_i': 10, 'u_i': 3.7777},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.116901, 0.070140, 0.042084, 0.025251, 0.015150], 'p_i': 20, 'u_i': 2.9102},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [2.311979, 1.387187, 0.832312, 0.499387], 'p_i': 40, 'u_i': 3.0744},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [9.021561, 5.412937], 'p_i': 80, 'u_i': 3.1102},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.426322, 0.255793, 0.153476, 0.092085, 0.055251, 0.033151], 'p_i': 20, 'u_i': 3.9746},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.480821, 0.288493, 0.173096], 'p_i': 10, 'u_i': 1.5757},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.738549, 0.443129, 0.265878], 'p_i': 40, 'u_i': 4.9941},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.701534, 0.420921], 'p_i': 40, 'u_i': 1.7632},
    ]
    B_BUDGET = 88.319993
    return processors, tasks, B_BUDGET

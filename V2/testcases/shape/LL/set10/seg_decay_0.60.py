"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 31, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.221612, 'e_o_k': [0.046491, 0.027895, 0.016737, 0.010042, 0.006025, 0.003615], 'p_i': 10, 'u_i': 3.7777},
        {'id': 1, 'e_m': 0.192518, 'e_o_k': [0.041750, 0.025050, 0.015030, 0.009018, 0.005411], 'p_i': 20, 'u_i': 2.9102},
        {'id': 2, 'e_m': 3.593476, 'e_o_k': [0.825707, 0.495424, 0.297254, 0.178353], 'p_i': 40, 'u_i': 3.0744},
        {'id': 3, 'e_m': 10.310356, 'e_o_k': [3.221986, 1.933192], 'p_i': 80, 'u_i': 3.1102},
        {'id': 4, 'e_m': 0.725770, 'e_o_k': [0.152258, 0.091355, 0.054813, 0.032888, 0.019733, 0.011840], 'p_i': 20, 'u_i': 3.9746},
        {'id': 5, 'e_m': 0.673150, 'e_o_k': [0.171722, 0.103033, 0.061820], 'p_i': 10, 'u_i': 1.5757},
        {'id': 6, 'e_m': 1.033969, 'e_o_k': [0.263767, 0.158260, 0.094956], 'p_i': 40, 'u_i': 4.9941},
        {'id': 7, 'e_m': 0.801753, 'e_o_k': [0.250548, 0.150329], 'p_i': 40, 'u_i': 1.7632},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1082, "set": 82, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.844903, 'e_o_k': [0.236573, 0.236573, 0.236573, 0.236573, 0.236573], 'p_i': 10, 'u_i': 3.8434},
        {'id': 1, 'e_m': 0.177585, 'e_o_k': [0.124309, 0.124309], 'p_i': 20, 'u_i': 3.7460},
        {'id': 2, 'e_m': 1.433543, 'e_o_k': [0.501740, 0.501740, 0.501740, 0.501740], 'p_i': 40, 'u_i': 2.3844},
        {'id': 3, 'e_m': 1.748862, 'e_o_k': [1.224203, 1.224203], 'p_i': 80, 'u_i': 3.6397},
        {'id': 4, 'e_m': 6.915032, 'e_o_k': [1.613507, 1.613507, 1.613507, 1.613507, 1.613507, 1.613507], 'p_i': 80, 'u_i': 2.0089},
        {'id': 5, 'e_m': 1.550765, 'e_o_k': [0.542768, 0.542768, 0.542768, 0.542768], 'p_i': 20, 'u_i': 4.2973},
        {'id': 6, 'e_m': 0.111141, 'e_o_k': [0.077798, 0.077798], 'p_i': 10, 'u_i': 3.5880},
        {'id': 7, 'e_m': 1.476817, 'e_o_k': [0.344591, 0.344591, 0.344591, 0.344591, 0.344591, 0.344591], 'p_i': 20, 'u_i': 4.0384},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 30, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.533781, 'e_o_k': [0.053378, 0.053378, 0.053378, 0.053378, 0.053378], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 3.051801, 'e_o_k': [0.762950, 0.762950], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 2.268878, 'e_o_k': [0.567219, 0.567219], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 2.027473, 'e_o_k': [0.168956, 0.168956, 0.168956, 0.168956, 0.168956, 0.168956], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.174589, 'e_o_k': [0.043647, 0.043647], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.345496, 'e_o_k': [0.057583, 0.057583, 0.057583], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 2.718295, 'e_o_k': [0.339787, 0.339787, 0.339787, 0.339787], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 1.388352, 'e_o_k': [0.231392, 0.231392, 0.231392], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET

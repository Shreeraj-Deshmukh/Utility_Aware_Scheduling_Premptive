"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.353209, 'e_o_k': [0.202661, 0.162129, 0.129703], 'p_i': 10, 'u_i': 4.9794},
        {'id': 1, 'e_m': 3.472957, 'e_o_k': [1.317910, 1.054328, 0.843462, 0.674770, 0.539816, 0.431853], 'p_i': 20, 'u_i': 1.8563},
        {'id': 2, 'e_m': 2.131727, 'e_o_k': [0.808943, 0.647155, 0.517724, 0.414179, 0.331343, 0.265075], 'p_i': 40, 'u_i': 1.0975},
        {'id': 3, 'e_m': 14.279303, 'e_o_k': [6.772027, 5.417622, 4.334097, 3.467278], 'p_i': 80, 'u_i': 4.1970},
        {'id': 4, 'e_m': 0.921014, 'e_o_k': [0.349504, 0.279603, 0.223683, 0.178946, 0.143157, 0.114526], 'p_i': 10, 'u_i': 1.7417},
        {'id': 5, 'e_m': 5.342908, 'e_o_k': [2.225152, 1.780122, 1.424097, 1.139278, 0.911422], 'p_i': 20, 'u_i': 3.7063},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET

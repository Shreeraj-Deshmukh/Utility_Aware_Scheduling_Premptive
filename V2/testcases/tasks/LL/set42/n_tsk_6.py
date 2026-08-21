"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.969754, 'e_o_k': [0.144240, 0.115392, 0.092314, 0.073851, 0.059081], 'p_i': 10, 'u_i': 2.8937},
        {'id': 1, 'e_m': 1.381909, 'e_o_k': [0.234063, 0.187251, 0.149800, 0.119840], 'p_i': 20, 'u_i': 3.5048},
        {'id': 2, 'e_m': 0.206917, 'e_o_k': [0.028043, 0.022434, 0.017948, 0.014358, 0.011486, 0.009189], 'p_i': 40, 'u_i': 4.5166},
        {'id': 3, 'e_m': 1.087762, 'e_o_k': [0.184242, 0.147393, 0.117915, 0.094332], 'p_i': 80, 'u_i': 1.0922},
        {'id': 4, 'e_m': 4.395290, 'e_o_k': [1.220914, 0.976731], 'p_i': 40, 'u_i': 2.4300},
        {'id': 5, 'e_m': 2.105539, 'e_o_k': [0.313175, 0.250540, 0.200432, 0.160346, 0.128277], 'p_i': 20, 'u_i': 4.3958},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET

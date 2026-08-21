"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1028, "set": 28, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.906412, 'e_o_k': [0.153525, 0.122820, 0.098256, 0.078605], 'p_i': 10, 'u_i': 4.1031},
        {'id': 1, 'e_m': 2.305692, 'e_o_k': [0.472478, 0.377982, 0.302386], 'p_i': 20, 'u_i': 2.8661},
        {'id': 2, 'e_m': 2.876100, 'e_o_k': [0.389792, 0.311833, 0.249467, 0.199573, 0.159659, 0.127727], 'p_i': 40, 'u_i': 2.5404},
        {'id': 3, 'e_m': 9.773732, 'e_o_k': [2.002814, 1.602251, 1.281801], 'p_i': 80, 'u_i': 1.0986},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET

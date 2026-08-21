"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.073055, 'e_o_k': [0.424806, 0.339845, 0.271876], 'p_i': 10, 'u_i': 2.4204},
        {'id': 1, 'e_m': 0.267192, 'e_o_k': [0.036212, 0.028970, 0.023176, 0.018540, 0.014832, 0.011866], 'p_i': 20, 'u_i': 4.6440},
        {'id': 2, 'e_m': 1.486671, 'e_o_k': [0.201485, 0.161188, 0.128951, 0.103160, 0.082528, 0.066023], 'p_i': 40, 'u_i': 4.0628},
        {'id': 3, 'e_m': 11.373449, 'e_o_k': [1.691672, 1.353338, 1.082670, 0.866136, 0.692909], 'p_i': 80, 'u_i': 1.2692},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET

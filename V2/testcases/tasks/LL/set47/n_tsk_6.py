"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.592557, 'e_o_k': [0.442377, 0.353901], 'p_i': 10, 'u_i': 1.2617},
        {'id': 1, 'e_m': 1.046846, 'e_o_k': [0.141877, 0.113501, 0.090801, 0.072641, 0.058113, 0.046490], 'p_i': 20, 'u_i': 4.5683},
        {'id': 2, 'e_m': 1.705304, 'e_o_k': [0.231116, 0.184893, 0.147914, 0.118331, 0.094665, 0.075732], 'p_i': 40, 'u_i': 2.4732},
        {'id': 3, 'e_m': 3.670607, 'e_o_k': [0.497469, 0.397975, 0.318380, 0.254704, 0.203763, 0.163011], 'p_i': 80, 'u_i': 3.5676},
        {'id': 4, 'e_m': 1.271002, 'e_o_k': [0.353056, 0.282445], 'p_i': 20, 'u_i': 2.3263},
        {'id': 5, 'e_m': 0.726735, 'e_o_k': [0.201871, 0.161497], 'p_i': 20, 'u_i': 1.7445},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319999, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319999, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.592557, 'e_o_k': [1.238655, 0.990924], 'p_i': 10, 'u_i': 1.2617},
        {'id': 1, 'e_m': 1.046846, 'e_o_k': [0.397255, 0.317804, 0.254243, 0.203394, 0.162716, 0.130172], 'p_i': 20, 'u_i': 4.5683},
        {'id': 2, 'e_m': 1.705304, 'e_o_k': [0.647125, 0.517700, 0.414160, 0.331328, 0.265062, 0.212050], 'p_i': 40, 'u_i': 2.4732},
        {'id': 3, 'e_m': 3.670607, 'e_o_k': [1.392914, 1.114331, 0.891465, 0.713172, 0.570538, 0.456430], 'p_i': 80, 'u_i': 3.5676},
        {'id': 4, 'e_m': 1.271002, 'e_o_k': [0.988557, 0.790846], 'p_i': 20, 'u_i': 2.3263},
        {'id': 5, 'e_m': 0.726735, 'e_o_k': [0.565238, 0.452191], 'p_i': 20, 'u_i': 1.7445},
    ]
    B_BUDGET = 88.319999
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399988, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399988, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.992272, 'e_o_k': [0.593805, 0.475044, 0.380035, 0.304028, 0.243223], 'p_i': 10, 'u_i': 1.6984},
        {'id': 1, 'e_m': 2.606367, 'e_o_k': [0.441458, 0.353166, 0.282533, 0.226026], 'p_i': 20, 'u_i': 3.4597},
        {'id': 2, 'e_m': 7.992473, 'e_o_k': [1.353739, 1.082991, 0.866393, 0.693114], 'p_i': 40, 'u_i': 4.7133},
        {'id': 3, 'e_m': 5.651409, 'e_o_k': [0.765923, 0.612738, 0.490191, 0.392153, 0.313722, 0.250978], 'p_i': 80, 'u_i': 2.1441},
    ]
    B_BUDGET = 110.399988
    return processors, tasks, B_BUDGET

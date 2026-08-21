"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399986, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.971116, 'e_o_k': [0.441920, 0.353536, 0.282829, 0.226263, 0.181010], 'p_i': 10, 'u_i': 1.3731},
        {'id': 1, 'e_m': 7.668867, 'e_o_k': [1.571489, 1.257191, 1.005753], 'p_i': 20, 'u_i': 1.2580},
        {'id': 2, 'e_m': 2.097251, 'e_o_k': [0.355225, 0.284180, 0.227344, 0.181875], 'p_i': 40, 'u_i': 4.0597},
        {'id': 3, 'e_m': 5.361097, 'e_o_k': [0.797403, 0.637922, 0.510338, 0.408270, 0.326616], 'p_i': 80, 'u_i': 2.2779},
    ]
    B_BUDGET = 110.399986
    return processors, tasks, B_BUDGET

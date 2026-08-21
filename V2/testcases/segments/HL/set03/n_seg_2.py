"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 27, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1003, "set": 3, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.759727, 'e_o_k': [0.211035, 0.168828], 'p_i': 10, 'u_i': 3.3255},
        {'id': 1, 'e_m': 2.267234, 'e_o_k': [0.629787, 0.503830], 'p_i': 20, 'u_i': 3.5739},
        {'id': 2, 'e_m': 1.540180, 'e_o_k': [0.427828, 0.342262], 'p_i': 40, 'u_i': 2.2786},
        {'id': 3, 'e_m': 8.351708, 'e_o_k': [2.319919, 1.855935], 'p_i': 80, 'u_i': 1.5604},
        {'id': 4, 'e_m': 8.673789, 'e_o_k': [2.409386, 1.927509], 'p_i': 80, 'u_i': 1.1253},
        {'id': 5, 'e_m': 24.118641, 'e_o_k': [6.699623, 5.359698], 'p_i': 80, 'u_i': 3.7966},
        {'id': 6, 'e_m': 0.384822, 'e_o_k': [0.106895, 0.085516], 'p_i': 10, 'u_i': 1.2428},
        {'id': 7, 'e_m': 0.775086, 'e_o_k': [0.215302, 0.172241], 'p_i': 40, 'u_i': 4.6455},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET

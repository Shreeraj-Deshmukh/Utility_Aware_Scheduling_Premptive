"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.722559, 'e_o_k': [0.122385, 0.097908, 0.078326, 0.062661], 'p_i': 10, 'u_i': 3.6067},
        {'id': 1, 'e_m': 5.886831, 'e_o_k': [1.206318, 0.965054, 0.772043], 'p_i': 20, 'u_i': 2.3971},
        {'id': 2, 'e_m': 5.724986, 'e_o_k': [0.851527, 0.681222, 0.544977, 0.435982, 0.348785], 'p_i': 40, 'u_i': 3.3740},
        {'id': 3, 'e_m': 23.222228, 'e_o_k': [6.450619, 5.160495], 'p_i': 80, 'u_i': 3.0150},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET

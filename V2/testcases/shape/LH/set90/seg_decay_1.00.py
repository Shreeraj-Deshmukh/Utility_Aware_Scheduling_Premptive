"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319978, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.319978, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1090, "set": 90, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.427962, 'e_o_k': [0.119829, 0.119829, 0.119829, 0.119829, 0.119829], 'p_i': 10, 'u_i': 3.1824},
        {'id': 1, 'e_m': 1.031123, 'e_o_k': [0.240595, 0.240595, 0.240595, 0.240595, 0.240595, 0.240595], 'p_i': 20, 'u_i': 3.3367},
        {'id': 2, 'e_m': 0.898123, 'e_o_k': [0.419124, 0.419124, 0.419124], 'p_i': 40, 'u_i': 4.5472},
        {'id': 3, 'e_m': 0.364547, 'e_o_k': [0.127591, 0.127591, 0.127591, 0.127591], 'p_i': 80, 'u_i': 1.6834},
        {'id': 4, 'e_m': 1.110849, 'e_o_k': [0.777594, 0.777594], 'p_i': 40, 'u_i': 3.8684},
        {'id': 5, 'e_m': 6.962867, 'e_o_k': [4.874007, 4.874007], 'p_i': 40, 'u_i': 4.7513},
        {'id': 6, 'e_m': 2.975430, 'e_o_k': [0.694267, 0.694267, 0.694267, 0.694267, 0.694267, 0.694267], 'p_i': 40, 'u_i': 2.4512},
        {'id': 7, 'e_m': 0.024091, 'e_o_k': [0.016864, 0.016864], 'p_i': 10, 'u_i': 1.4858},
    ]
    B_BUDGET = 88.319978
    return processors, tasks, B_BUDGET

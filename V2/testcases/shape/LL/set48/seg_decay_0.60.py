"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 29, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.686006, 'e_o_k': [0.214377, 0.128626], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 1.744166, 'e_o_k': [0.444940, 0.266964, 0.160179], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.047982, 'e_o_k': [0.012240, 0.007344, 0.004407], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 1.929764, 'e_o_k': [0.603051, 0.361831], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 5.818863, 'e_o_k': [1.818395, 1.091037], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 1.092627, 'e_o_k': [0.236951, 0.142170, 0.085302, 0.051181, 0.030709], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 0.842076, 'e_o_k': [0.182615, 0.109569, 0.065742, 0.039445, 0.023667], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 0.583581, 'e_o_k': [0.126557, 0.075934, 0.045561, 0.027336, 0.016402], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET

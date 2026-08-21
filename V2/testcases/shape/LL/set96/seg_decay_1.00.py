"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199962, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 55.199962, "H": 80, "J": 32, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.252893, 'e_o_k': [0.063223, 0.063223], 'p_i': 10, 'u_i': 2.8589},
        {'id': 1, 'e_m': 0.097609, 'e_o_k': [0.016268, 0.016268, 0.016268], 'p_i': 20, 'u_i': 2.7598},
        {'id': 2, 'e_m': 5.092114, 'e_o_k': [1.273028, 1.273028], 'p_i': 40, 'u_i': 2.0735},
        {'id': 3, 'e_m': 3.280589, 'e_o_k': [0.273382, 0.273382, 0.273382, 0.273382, 0.273382, 0.273382], 'p_i': 80, 'u_i': 3.6242},
        {'id': 4, 'e_m': 2.269701, 'e_o_k': [0.567425, 0.567425], 'p_i': 20, 'u_i': 2.1240},
        {'id': 5, 'e_m': 3.382746, 'e_o_k': [0.422843, 0.422843, 0.422843, 0.422843], 'p_i': 80, 'u_i': 2.2796},
        {'id': 6, 'e_m': 0.542314, 'e_o_k': [0.054231, 0.054231, 0.054231, 0.054231, 0.054231], 'p_i': 20, 'u_i': 4.8637},
        {'id': 7, 'e_m': 0.186349, 'e_o_k': [0.031058, 0.031058, 0.031058], 'p_i': 10, 'u_i': 2.9768},
    ]
    B_BUDGET = 55.199962
    return processors, tasks, B_BUDGET

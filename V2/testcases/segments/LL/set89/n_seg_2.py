"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 47, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 47, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1089, "set": 89, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.612231, 'e_o_k': [0.170064, 0.136051], 'p_i': 10, 'u_i': 3.9801},
        {'id': 1, 'e_m': 0.818720, 'e_o_k': [0.227422, 0.181938], 'p_i': 20, 'u_i': 3.7892},
        {'id': 2, 'e_m': 1.130553, 'e_o_k': [0.314043, 0.251234], 'p_i': 40, 'u_i': 1.4880},
        {'id': 3, 'e_m': 0.013730, 'e_o_k': [0.003814, 0.003051], 'p_i': 80, 'u_i': 4.5731},
        {'id': 4, 'e_m': 0.810047, 'e_o_k': [0.225013, 0.180010], 'p_i': 10, 'u_i': 3.7064},
        {'id': 5, 'e_m': 1.453435, 'e_o_k': [0.403732, 0.322986], 'p_i': 10, 'u_i': 4.7396},
        {'id': 6, 'e_m': 0.030685, 'e_o_k': [0.008524, 0.006819], 'p_i': 10, 'u_i': 4.0832},
        {'id': 7, 'e_m': 0.399887, 'e_o_k': [0.111080, 0.088864], 'p_i': 10, 'u_i': 1.4400},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET

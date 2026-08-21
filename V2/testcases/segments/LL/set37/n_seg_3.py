"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200018, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200018, "H": 80, "J": 33, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.190797, 'e_o_k': [0.244016, 0.195213, 0.156170], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.359142, 'e_o_k': [0.073595, 0.058876, 0.047101], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 0.831853, 'e_o_k': [0.170462, 0.136369, 0.109095], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 10.420760, 'e_o_k': [2.135402, 1.708321, 1.366657], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 0.657127, 'e_o_k': [0.134657, 0.107726, 0.086181], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.368053, 'e_o_k': [0.075421, 0.060337, 0.048269], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 0.634198, 'e_o_k': [0.129959, 0.103967, 0.083174], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 0.421433, 'e_o_k': [0.086359, 0.069087, 0.055270], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 55.200018
    return processors, tasks, B_BUDGET

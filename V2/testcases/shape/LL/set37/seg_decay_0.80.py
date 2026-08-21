"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199995, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}
"""

_SPEC = '{"B": 55.199995, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "shape", "util_per_core": 0.2, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.190797, 'e_o_k': [0.330777, 0.264621], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.359142, 'e_o_k': [0.060830, 0.048664, 0.038931, 0.031145], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 0.831853, 'e_o_k': [0.123729, 0.098983, 0.079186, 0.063349, 0.050679], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 10.420760, 'e_o_k': [1.765034, 1.412027, 1.129622, 0.903697], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 0.657127, 'e_o_k': [0.182535, 0.146028], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.368053, 'e_o_k': [0.054744, 0.043795, 0.035036, 0.028029, 0.022423], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 0.634198, 'e_o_k': [0.129959, 0.103967, 0.083174], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 0.421433, 'e_o_k': [0.062683, 0.050147, 0.040117, 0.032094, 0.025675], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 55.199995
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760008, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760008, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.786195, 'e_o_k': [0.297699, 0.238159], 'p_i': 10, 'u_i': 3.1340},
        {'id': 1, 'e_m': 0.538714, 'e_o_k': [0.054747, 0.043798, 0.035038, 0.028031], 'p_i': 20, 'u_i': 4.7064},
        {'id': 2, 'e_m': 1.247780, 'e_o_k': [0.111356, 0.089085, 0.071268, 0.057014, 0.045611], 'p_i': 40, 'u_i': 3.9461},
        {'id': 3, 'e_m': 15.631140, 'e_o_k': [1.588531, 1.270824, 1.016660, 0.813328], 'p_i': 80, 'u_i': 2.2173},
        {'id': 4, 'e_m': 0.985690, 'e_o_k': [0.164282, 0.131425], 'p_i': 20, 'u_i': 4.4667},
        {'id': 5, 'e_m': 0.552080, 'e_o_k': [0.049269, 0.039416, 0.031532, 0.025226, 0.020181], 'p_i': 10, 'u_i': 3.9626},
        {'id': 6, 'e_m': 0.951298, 'e_o_k': [0.116963, 0.093570, 0.074856], 'p_i': 20, 'u_i': 1.6271},
        {'id': 7, 'e_m': 0.632150, 'e_o_k': [0.056415, 0.045132, 0.036106, 0.028885, 0.023108], 'p_i': 40, 'u_i': 2.4987},
    ]
    B_BUDGET = 71.760008
    return processors, tasks, B_BUDGET

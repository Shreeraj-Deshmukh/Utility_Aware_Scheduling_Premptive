"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 72.864001, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.7, "seed": 1011, "set": 11, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}
"""

_SPEC = '{"B": 72.864001, "H": 80, "J": 30, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 0.7, "seed": 1011, "set": 11, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.533781, 'e_o_k': [0.222303, 0.177842, 0.142274, 0.113819, 0.091055], 'p_i': 10, 'u_i': 4.6830},
        {'id': 1, 'e_m': 3.051801, 'e_o_k': [2.373623, 1.898898], 'p_i': 20, 'u_i': 2.4027},
        {'id': 2, 'e_m': 2.268878, 'e_o_k': [1.764683, 1.411746], 'p_i': 40, 'u_i': 2.7203},
        {'id': 3, 'e_m': 2.027473, 'e_o_k': [0.769381, 0.615505, 0.492404, 0.393923, 0.315138, 0.252111], 'p_i': 80, 'u_i': 2.4000},
        {'id': 4, 'e_m': 0.174589, 'e_o_k': [0.135792, 0.108633], 'p_i': 20, 'u_i': 2.9059},
        {'id': 5, 'e_m': 0.345496, 'e_o_k': [0.198235, 0.158588, 0.126871], 'p_i': 10, 'u_i': 3.1411},
        {'id': 6, 'e_m': 2.718295, 'e_o_k': [1.289164, 1.031331, 0.825065, 0.660052], 'p_i': 80, 'u_i': 3.1206},
        {'id': 7, 'e_m': 1.388352, 'e_o_k': [0.796595, 0.637276, 0.509821], 'p_i': 40, 'u_i': 4.7030},
    ]
    B_BUDGET = 72.864001
    return processors, tasks, B_BUDGET

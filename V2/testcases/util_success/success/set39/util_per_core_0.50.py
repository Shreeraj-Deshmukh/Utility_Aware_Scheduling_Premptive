"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600003, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600003, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.544156, 'e_o_k': [0.090693, 0.072554], 'p_i': 10, 'u_i': 1.4412},
        {'id': 1, 'e_m': 4.615521, 'e_o_k': [0.469057, 0.375246, 0.300196, 0.240157], 'p_i': 20, 'u_i': 3.7136},
        {'id': 2, 'e_m': 2.077244, 'e_o_k': [0.168915, 0.135132, 0.108105, 0.086484, 0.069187, 0.055350], 'p_i': 40, 'u_i': 3.0715},
        {'id': 3, 'e_m': 27.350056, 'e_o_k': [2.224016, 1.779213, 1.423370, 1.138696, 0.910957, 0.728765], 'p_i': 80, 'u_i': 2.1053},
        {'id': 4, 'e_m': 0.219733, 'e_o_k': [0.036622, 0.029298], 'p_i': 20, 'u_i': 3.9261},
        {'id': 5, 'e_m': 0.665000, 'e_o_k': [0.110833, 0.088667], 'p_i': 20, 'u_i': 2.2961},
        {'id': 6, 'e_m': 0.214314, 'e_o_k': [0.019126, 0.015301, 0.012241, 0.009793, 0.007834], 'p_i': 10, 'u_i': 1.3761},
        {'id': 7, 'e_m': 5.106670, 'e_o_k': [0.627869, 0.502295, 0.401836], 'p_i': 20, 'u_i': 2.1930},
    ]
    B_BUDGET = 119.600003
    return processors, tasks, B_BUDGET

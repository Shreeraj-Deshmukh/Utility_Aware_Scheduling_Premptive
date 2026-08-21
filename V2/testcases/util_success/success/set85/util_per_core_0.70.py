"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.44, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.44, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.905041, 'e_o_k': [0.480128, 0.384102, 0.307282], 'p_i': 10, 'u_i': 2.7743},
        {'id': 1, 'e_m': 5.385044, 'e_o_k': [0.547261, 0.437808, 0.350247, 0.280197], 'p_i': 20, 'u_i': 3.3191},
        {'id': 2, 'e_m': 11.788583, 'e_o_k': [1.449416, 1.159533, 0.927626], 'p_i': 40, 'u_i': 1.2504},
        {'id': 3, 'e_m': 28.549819, 'e_o_k': [2.321576, 1.857261, 1.485809, 1.188647, 0.950918, 0.760734], 'p_i': 80, 'u_i': 1.6478},
        {'id': 4, 'e_m': 0.216441, 'e_o_k': [0.019316, 0.015453, 0.012362, 0.009890, 0.007912], 'p_i': 10, 'u_i': 4.3413},
        {'id': 5, 'e_m': 0.444233, 'e_o_k': [0.054619, 0.043695, 0.034956], 'p_i': 20, 'u_i': 1.0636},
        {'id': 6, 'e_m': 0.684637, 'e_o_k': [0.061099, 0.048879, 0.039104, 0.031283, 0.025026], 'p_i': 20, 'u_i': 4.5969},
        {'id': 7, 'e_m': 0.211375, 'e_o_k': [0.025989, 0.020791, 0.016633], 'p_i': 20, 'u_i': 3.6081},
    ]
    B_BUDGET = 167.440000
    return processors, tasks, B_BUDGET

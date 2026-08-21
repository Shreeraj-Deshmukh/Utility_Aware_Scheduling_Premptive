"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600003, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600003, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1000, "set": 0, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.353399, 'e_o_k': [0.031538, 0.025231, 0.020185, 0.016148, 0.012918], 'p_i': 10, 'u_i': 4.9222},
        {'id': 1, 'e_m': 1.246497, 'e_o_k': [0.126676, 0.101341, 0.081073, 0.064858], 'p_i': 20, 'u_i': 1.9107},
        {'id': 2, 'e_m': 13.359333, 'e_o_k': [1.192230, 0.953784, 0.763027, 0.610422, 0.488337], 'p_i': 40, 'u_i': 1.7322},
        {'id': 3, 'e_m': 10.421875, 'e_o_k': [0.930082, 0.744065, 0.595252, 0.476202, 0.380961], 'p_i': 80, 'u_i': 1.5709},
        {'id': 4, 'e_m': 1.959590, 'e_o_k': [0.174880, 0.139904, 0.111923, 0.089539, 0.071631], 'p_i': 20, 'u_i': 3.7661},
        {'id': 5, 'e_m': 1.828231, 'e_o_k': [0.224783, 0.179826, 0.143861], 'p_i': 20, 'u_i': 1.0932},
        {'id': 6, 'e_m': 0.107885, 'e_o_k': [0.008773, 0.007018, 0.005615, 0.004492, 0.003593, 0.002875], 'p_i': 20, 'u_i': 2.8740},
        {'id': 7, 'e_m': 9.731728, 'e_o_k': [1.196524, 0.957219, 0.765775], 'p_i': 40, 'u_i': 4.9324},
    ]
    B_BUDGET = 119.600003
    return processors, tasks, B_BUDGET

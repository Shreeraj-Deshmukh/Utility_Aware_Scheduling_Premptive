"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759994, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759994, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.815748, 'e_o_k': [0.135958, 0.108766], 'p_i': 10, 'u_i': 2.8418},
        {'id': 1, 'e_m': 0.293948, 'e_o_k': [0.029873, 0.023898, 0.019119, 0.015295], 'p_i': 20, 'u_i': 1.5566},
        {'id': 2, 'e_m': 9.822108, 'e_o_k': [0.998182, 0.798545, 0.638836, 0.511069], 'p_i': 40, 'u_i': 3.2695},
        {'id': 3, 'e_m': 5.741333, 'e_o_k': [0.956889, 0.765511], 'p_i': 80, 'u_i': 3.8342},
        {'id': 4, 'e_m': 0.227868, 'e_o_k': [0.018529, 0.014824, 0.011859, 0.009487, 0.007590, 0.006072], 'p_i': 20, 'u_i': 4.3734},
        {'id': 5, 'e_m': 0.566037, 'e_o_k': [0.057524, 0.046019, 0.036815, 0.029452], 'p_i': 20, 'u_i': 3.3497},
        {'id': 6, 'e_m': 3.774863, 'e_o_k': [0.383624, 0.306899, 0.245520, 0.196416], 'p_i': 40, 'u_i': 4.2042},
        {'id': 7, 'e_m': 2.093664, 'e_o_k': [0.257418, 0.205934, 0.164747], 'p_i': 40, 'u_i': 1.0373},
    ]
    B_BUDGET = 71.759994
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200009, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200009, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1002, "set": 2, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.779005, 'e_o_k': [0.296501, 0.237201], 'p_i': 10, 'u_i': 2.6844},
        {'id': 1, 'e_m': 4.890096, 'e_o_k': [0.397646, 0.318117, 0.254494, 0.203595, 0.162876, 0.130301], 'p_i': 20, 'u_i': 3.2251},
        {'id': 2, 'e_m': 16.447269, 'e_o_k': [2.022205, 1.617764, 1.294211], 'p_i': 40, 'u_i': 4.0273},
        {'id': 3, 'e_m': 37.245780, 'e_o_k': [4.579399, 3.663519, 2.930815], 'p_i': 80, 'u_i': 2.2476},
        {'id': 4, 'e_m': 12.047755, 'e_o_k': [1.224365, 0.979492, 0.783594, 0.626875], 'p_i': 80, 'u_i': 1.3199},
        {'id': 5, 'e_m': 1.148591, 'e_o_k': [0.093400, 0.074720, 0.059776, 0.047821, 0.038256, 0.030605], 'p_i': 10, 'u_i': 4.7520},
        {'id': 6, 'e_m': 3.299155, 'e_o_k': [0.294427, 0.235542, 0.188433, 0.150747, 0.120597], 'p_i': 20, 'u_i': 3.4892},
        {'id': 7, 'e_m': 5.408539, 'e_o_k': [0.901423, 0.721139], 'p_i': 20, 'u_i': 1.4050},
    ]
    B_BUDGET = 239.200009
    return processors, tasks, B_BUDGET

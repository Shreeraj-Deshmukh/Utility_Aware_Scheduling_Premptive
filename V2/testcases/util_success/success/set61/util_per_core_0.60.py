"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.52, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.52, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.028869, 'e_o_k': [0.104560, 0.083648, 0.066918, 0.053535], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 3.726613, 'e_o_k': [0.378721, 0.302977, 0.242381, 0.193905], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.072106, 'e_o_k': [0.006435, 0.005148, 0.004118, 0.003295, 0.002636], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 16.982020, 'e_o_k': [1.725815, 1.380652, 1.104522, 0.883617], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 14.794469, 'e_o_k': [2.465745, 1.972596], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 4.810744, 'e_o_k': [0.429326, 0.343461, 0.274769, 0.219815, 0.175852], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 14.410580, 'e_o_k': [1.286047, 1.028837, 0.823070, 0.658456, 0.526765], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 2.115355, 'e_o_k': [0.214975, 0.171980, 0.137584, 0.110067], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 143.520000
    return processors, tasks, B_BUDGET

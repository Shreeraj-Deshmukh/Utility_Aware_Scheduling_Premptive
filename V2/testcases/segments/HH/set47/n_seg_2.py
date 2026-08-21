"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 41, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.433436, 'e_o_k': [1.892672, 1.514138], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 1.678664, 'e_o_k': [1.305628, 1.044502], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 2.697717, 'e_o_k': [2.098225, 1.678580], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 5.583418, 'e_o_k': [4.342658, 3.474127], 'p_i': 80, 'u_i': 2.0127},
        {'id': 4, 'e_m': 0.959967, 'e_o_k': [0.746641, 0.597313], 'p_i': 10, 'u_i': 4.7864},
        {'id': 5, 'e_m': 1.200367, 'e_o_k': [0.933618, 0.746895], 'p_i': 10, 'u_i': 1.7550},
        {'id': 6, 'e_m': 0.195327, 'e_o_k': [0.151921, 0.121537], 'p_i': 10, 'u_i': 2.9364},
        {'id': 7, 'e_m': 3.996858, 'e_o_k': [3.108668, 2.486934], 'p_i': 40, 'u_i': 1.0429},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET

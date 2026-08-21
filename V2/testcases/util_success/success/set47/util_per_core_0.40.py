"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680021, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680021, "H": 80, "J": 41, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.433436, 'e_o_k': [0.217168, 0.173734, 0.138987, 0.111190, 0.088952], 'p_i': 10, 'u_i': 3.4259},
        {'id': 1, 'e_m': 1.678664, 'e_o_k': [0.170596, 0.136477, 0.109181, 0.087345], 'p_i': 20, 'u_i': 1.3819},
        {'id': 2, 'e_m': 2.697717, 'e_o_k': [0.449620, 0.359696], 'p_i': 40, 'u_i': 1.7445},
        {'id': 3, 'e_m': 5.583418, 'e_o_k': [0.454025, 0.363220, 0.290576, 0.232461, 0.185969, 0.148775], 'p_i': 80, 'u_i': 3.6642},
        {'id': 4, 'e_m': 0.959967, 'e_o_k': [0.097558, 0.078046, 0.062437, 0.049949], 'p_i': 10, 'u_i': 2.6174},
        {'id': 5, 'e_m': 1.200367, 'e_o_k': [0.107125, 0.085700, 0.068560, 0.054848, 0.043878], 'p_i': 10, 'u_i': 2.3254},
        {'id': 6, 'e_m': 0.195327, 'e_o_k': [0.032555, 0.026044], 'p_i': 10, 'u_i': 3.2626},
        {'id': 7, 'e_m': 3.996858, 'e_o_k': [0.356693, 0.285354, 0.228283, 0.182627, 0.146101], 'p_i': 40, 'u_i': 1.6837},
    ]
    B_BUDGET = 95.680021
    return processors, tasks, B_BUDGET

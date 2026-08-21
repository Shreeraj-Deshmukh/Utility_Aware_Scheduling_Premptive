"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199991, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199991, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1047, "set": 47, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.900270, 'e_o_k': [0.073207, 0.058566, 0.046852, 0.037482, 0.029986, 0.023988], 'p_i': 10, 'u_i': 2.3485},
        {'id': 1, 'e_m': 9.335348, 'e_o_k': [0.759120, 0.607296, 0.485836, 0.388669, 0.310935, 0.248748], 'p_i': 20, 'u_i': 4.6143},
        {'id': 2, 'e_m': 6.667199, 'e_o_k': [1.111200, 0.888960], 'p_i': 40, 'u_i': 3.6010},
        {'id': 3, 'e_m': 28.229243, 'e_o_k': [4.704874, 3.763899], 'p_i': 80, 'u_i': 3.9719},
        {'id': 4, 'e_m': 2.406384, 'e_o_k': [0.244551, 0.195641, 0.156513, 0.125210], 'p_i': 10, 'u_i': 1.7124},
        {'id': 5, 'e_m': 0.739468, 'e_o_k': [0.075149, 0.060119, 0.048095, 0.038476], 'p_i': 40, 'u_i': 2.0839},
        {'id': 6, 'e_m': 35.547086, 'e_o_k': [3.612509, 2.890007, 2.312006, 1.849604], 'p_i': 80, 'u_i': 3.4011},
        {'id': 7, 'e_m': 4.403928, 'e_o_k': [0.733988, 0.587190], 'p_i': 20, 'u_i': 4.0659},
    ]
    B_BUDGET = 239.199991
    return processors, tasks, B_BUDGET

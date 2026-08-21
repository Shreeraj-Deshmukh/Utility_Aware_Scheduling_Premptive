"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120008, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120008, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.883015, 'e_o_k': [0.168046, 0.134437, 0.107550, 0.086040, 0.068832], 'p_i': 10, 'u_i': 1.3735},
        {'id': 1, 'e_m': 7.354146, 'e_o_k': [0.747373, 0.597898, 0.478318, 0.382655], 'p_i': 20, 'u_i': 1.0216},
        {'id': 2, 'e_m': 16.519541, 'e_o_k': [2.031091, 1.624873, 1.299898], 'p_i': 40, 'u_i': 2.5479},
        {'id': 3, 'e_m': 30.517411, 'e_o_k': [2.481575, 1.985260, 1.588208, 1.270566, 1.016453, 0.813162], 'p_i': 80, 'u_i': 1.6473},
        {'id': 4, 'e_m': 7.124183, 'e_o_k': [0.635785, 0.508628, 0.406902, 0.325522, 0.260418], 'p_i': 80, 'u_i': 4.0690},
        {'id': 5, 'e_m': 5.976970, 'e_o_k': [0.734873, 0.587899, 0.470319], 'p_i': 20, 'u_i': 4.0670},
        {'id': 6, 'e_m': 2.711685, 'e_o_k': [0.242000, 0.193600, 0.154880, 0.123904, 0.099123], 'p_i': 20, 'u_i': 1.4405},
        {'id': 7, 'e_m': 6.520999, 'e_o_k': [0.530266, 0.424213, 0.339370, 0.271496, 0.217197, 0.173758], 'p_i': 20, 'u_i': 4.2490},
    ]
    B_BUDGET = 263.120008
    return processors, tasks, B_BUDGET

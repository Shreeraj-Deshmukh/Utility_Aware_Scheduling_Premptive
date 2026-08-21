"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.36, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.36, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.246747, 'e_o_k': [0.276239, 0.220991, 0.176793], 'p_i': 10, 'u_i': 1.4405},
        {'id': 1, 'e_m': 2.065811, 'e_o_k': [0.209940, 0.167952, 0.134362, 0.107489], 'p_i': 20, 'u_i': 3.4151},
        {'id': 2, 'e_m': 2.061846, 'e_o_k': [0.209537, 0.167630, 0.134104, 0.107283], 'p_i': 40, 'u_i': 2.3956},
        {'id': 3, 'e_m': 20.215200, 'e_o_k': [1.804069, 1.443256, 1.154604, 0.923684, 0.738947], 'p_i': 80, 'u_i': 3.6029},
        {'id': 4, 'e_m': 0.702840, 'e_o_k': [0.071427, 0.057141, 0.045713, 0.036571], 'p_i': 10, 'u_i': 4.4783},
        {'id': 5, 'e_m': 8.080616, 'e_o_k': [1.346769, 1.077416], 'p_i': 40, 'u_i': 1.4735},
        {'id': 6, 'e_m': 2.204708, 'e_o_k': [0.271071, 0.216857, 0.173485], 'p_i': 10, 'u_i': 4.2633},
        {'id': 7, 'e_m': 38.002275, 'e_o_k': [3.090219, 2.472175, 1.977740, 1.582192, 1.265754, 1.012603], 'p_i': 80, 'u_i': 4.6185},
    ]
    B_BUDGET = 191.360000
    return processors, tasks, B_BUDGET

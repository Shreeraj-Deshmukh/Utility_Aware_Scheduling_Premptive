"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.12001, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.12001, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.519744, 'e_o_k': [0.052820, 0.042256, 0.033805, 0.027044], 'p_i': 10, 'u_i': 3.7145},
        {'id': 1, 'e_m': 9.528152, 'e_o_k': [1.171494, 0.937195, 0.749756], 'p_i': 20, 'u_i': 1.5869},
        {'id': 2, 'e_m': 2.965282, 'e_o_k': [0.364584, 0.291667, 0.233334], 'p_i': 40, 'u_i': 4.5179},
        {'id': 3, 'e_m': 8.376724, 'e_o_k': [0.851293, 0.681035, 0.544828, 0.435862], 'p_i': 80, 'u_i': 4.5220},
        {'id': 4, 'e_m': 9.579524, 'e_o_k': [1.177810, 0.942248, 0.753799], 'p_i': 20, 'u_i': 3.1960},
        {'id': 5, 'e_m': 39.950804, 'e_o_k': [4.911984, 3.929587, 3.143670], 'p_i': 80, 'u_i': 1.0258},
        {'id': 6, 'e_m': 0.668101, 'e_o_k': [0.054328, 0.043462, 0.034770, 0.027816, 0.022253, 0.017802], 'p_i': 20, 'u_i': 2.7860},
        {'id': 7, 'e_m': 38.480843, 'e_o_k': [3.434154, 2.747323, 2.197859, 1.758287, 1.406630], 'p_i': 80, 'u_i': 4.3037},
    ]
    B_BUDGET = 263.120010
    return processors, tasks, B_BUDGET

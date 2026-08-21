"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279999, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279999, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.304054, 'e_o_k': [0.132526, 0.106021, 0.084816, 0.067853], 'p_i': 10, 'u_i': 4.6704},
        {'id': 1, 'e_m': 0.168518, 'e_o_k': [0.028086, 0.022469], 'p_i': 20, 'u_i': 1.7142},
        {'id': 2, 'e_m': 16.676361, 'e_o_k': [2.050372, 1.640298, 1.312238], 'p_i': 40, 'u_i': 2.7421},
        {'id': 3, 'e_m': 20.570006, 'e_o_k': [1.672685, 1.338148, 1.070518, 0.856415, 0.685132, 0.548105], 'p_i': 80, 'u_i': 1.9194},
        {'id': 4, 'e_m': 8.522756, 'e_o_k': [1.420459, 1.136367], 'p_i': 20, 'u_i': 4.0448},
        {'id': 5, 'e_m': 6.990765, 'e_o_k': [0.859520, 0.687616, 0.550093], 'p_i': 20, 'u_i': 1.1256},
        {'id': 6, 'e_m': 0.231378, 'e_o_k': [0.023514, 0.018811, 0.015049, 0.012039], 'p_i': 10, 'u_i': 3.9028},
        {'id': 7, 'e_m': 3.766417, 'e_o_k': [0.336127, 0.268902, 0.215121, 0.172097, 0.137678], 'p_i': 20, 'u_i': 2.5194},
    ]
    B_BUDGET = 215.279999
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440009, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440009, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.920821, 'e_o_k': [0.156195, 0.124956, 0.099965, 0.079972, 0.063977, 0.051182], 'p_i': 10, 'u_i': 1.2398},
        {'id': 1, 'e_m': 2.446385, 'e_o_k': [0.248616, 0.198893, 0.159115, 0.127292], 'p_i': 20, 'u_i': 1.6455},
        {'id': 2, 'e_m': 4.252993, 'e_o_k': [0.432215, 0.345772, 0.276617, 0.221294], 'p_i': 40, 'u_i': 1.3745},
        {'id': 3, 'e_m': 3.158259, 'e_o_k': [0.388310, 0.310648, 0.248519], 'p_i': 80, 'u_i': 1.5038},
        {'id': 4, 'e_m': 3.359562, 'e_o_k': [0.413061, 0.330449, 0.264359], 'p_i': 10, 'u_i': 4.4242},
        {'id': 5, 'e_m': 3.035380, 'e_o_k': [0.505897, 0.404717], 'p_i': 10, 'u_i': 1.3856},
        {'id': 6, 'e_m': 4.434956, 'e_o_k': [0.739159, 0.591327], 'p_i': 40, 'u_i': 2.4453},
        {'id': 7, 'e_m': 7.577099, 'e_o_k': [0.676205, 0.540964, 0.432771, 0.346217, 0.276973], 'p_i': 40, 'u_i': 2.4405},
    ]
    B_BUDGET = 167.440009
    return processors, tasks, B_BUDGET

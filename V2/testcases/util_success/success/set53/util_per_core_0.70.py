"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440009, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440009, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1053, "set": 53, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.556607, 'e_o_k': [0.092768, 0.074214], 'p_i': 10, 'u_i': 1.8047},
        {'id': 1, 'e_m': 4.265890, 'e_o_k': [0.710982, 0.568785], 'p_i': 20, 'u_i': 1.0945},
        {'id': 2, 'e_m': 3.485272, 'e_o_k': [0.311037, 0.248830, 0.199064, 0.159251, 0.127401], 'p_i': 40, 'u_i': 2.4137},
        {'id': 3, 'e_m': 18.794522, 'e_o_k': [3.132420, 2.505936], 'p_i': 80, 'u_i': 1.6729},
        {'id': 4, 'e_m': 3.214710, 'e_o_k': [0.261410, 0.209128, 0.167302, 0.133842, 0.107073, 0.085659], 'p_i': 40, 'u_i': 2.8481},
        {'id': 5, 'e_m': 2.980120, 'e_o_k': [0.302858, 0.242286, 0.193829, 0.155063], 'p_i': 10, 'u_i': 3.6691},
        {'id': 6, 'e_m': 5.005765, 'e_o_k': [0.508716, 0.406973, 0.325578, 0.260463], 'p_i': 20, 'u_i': 3.0767},
        {'id': 7, 'e_m': 14.425079, 'e_o_k': [1.173000, 0.938400, 0.750720, 0.600576, 0.480461, 0.384368], 'p_i': 80, 'u_i': 1.7471},
    ]
    B_BUDGET = 167.440009
    return processors, tasks, B_BUDGET

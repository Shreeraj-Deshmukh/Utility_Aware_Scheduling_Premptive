"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520003, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.010259, 'e_o_k': [0.305921, 0.244736, 0.195789, 0.156631], 'p_i': 10, 'u_i': 2.9329},
        {'id': 1, 'e_m': 0.215790, 'e_o_k': [0.021930, 0.017544, 0.014035, 0.011228], 'p_i': 20, 'u_i': 4.3550},
        {'id': 2, 'e_m': 6.547925, 'e_o_k': [0.584358, 0.467486, 0.373989, 0.299191, 0.239353], 'p_i': 40, 'u_i': 2.2741},
        {'id': 3, 'e_m': 2.881721, 'e_o_k': [0.354310, 0.283448, 0.226758], 'p_i': 80, 'u_i': 2.5808},
        {'id': 4, 'e_m': 5.054064, 'e_o_k': [0.451041, 0.360833, 0.288666, 0.230933, 0.184746], 'p_i': 40, 'u_i': 4.5356},
        {'id': 5, 'e_m': 2.103630, 'e_o_k': [0.258643, 0.206914, 0.165532], 'p_i': 20, 'u_i': 4.4130},
        {'id': 6, 'e_m': 10.225689, 'e_o_k': [1.257257, 1.005806, 0.804644], 'p_i': 80, 'u_i': 1.1305},
        {'id': 7, 'e_m': 3.291108, 'e_o_k': [0.334462, 0.267570, 0.214056, 0.171245], 'p_i': 10, 'u_i': 4.7707},
    ]
    B_BUDGET = 143.520003
    return processors, tasks, B_BUDGET

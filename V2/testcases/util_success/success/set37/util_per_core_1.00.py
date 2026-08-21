"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.200013, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.200013, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1037, "set": 37, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.598533, 'e_o_k': [0.365705, 0.292564, 0.234051, 0.187241], 'p_i': 10, 'u_i': 4.7284},
        {'id': 1, 'e_m': 1.225688, 'e_o_k': [0.204281, 0.163425], 'p_i': 20, 'u_i': 2.9850},
        {'id': 2, 'e_m': 16.689130, 'e_o_k': [2.781522, 2.225217], 'p_i': 40, 'u_i': 4.6281},
        {'id': 3, 'e_m': 15.888104, 'e_o_k': [1.417905, 1.134324, 0.907460, 0.725968, 0.580774], 'p_i': 80, 'u_i': 1.0041},
        {'id': 4, 'e_m': 11.460008, 'e_o_k': [1.022728, 0.818182, 0.654546, 0.523637, 0.418909], 'p_i': 40, 'u_i': 2.2799},
        {'id': 5, 'e_m': 0.703447, 'e_o_k': [0.071489, 0.057191, 0.045753, 0.036602], 'p_i': 10, 'u_i': 4.7563},
        {'id': 6, 'e_m': 1.534275, 'e_o_k': [0.255713, 0.204570], 'p_i': 10, 'u_i': 4.7914},
        {'id': 7, 'e_m': 36.220823, 'e_o_k': [3.232463, 2.585970, 2.068776, 1.655021, 1.324017], 'p_i': 80, 'u_i': 4.0401},
    ]
    B_BUDGET = 239.200013
    return processors, tasks, B_BUDGET

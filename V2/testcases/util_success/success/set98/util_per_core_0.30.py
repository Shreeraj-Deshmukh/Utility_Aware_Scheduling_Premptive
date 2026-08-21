"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760008, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760008, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.316583, 'e_o_k': [0.107060, 0.085648, 0.068519, 0.054815, 0.043852, 0.035081], 'p_i': 10, 'u_i': 3.0970},
        {'id': 1, 'e_m': 0.939121, 'e_o_k': [0.095439, 0.076351, 0.061081, 0.048865], 'p_i': 20, 'u_i': 1.3215},
        {'id': 2, 'e_m': 3.574993, 'e_o_k': [0.439548, 0.351639, 0.281311], 'p_i': 40, 'u_i': 2.9112},
        {'id': 3, 'e_m': 0.147749, 'e_o_k': [0.013186, 0.010548, 0.008439, 0.006751, 0.005401], 'p_i': 80, 'u_i': 2.1467},
        {'id': 4, 'e_m': 0.054971, 'e_o_k': [0.004906, 0.003925, 0.003140, 0.002512, 0.002009], 'p_i': 10, 'u_i': 3.3563},
        {'id': 5, 'e_m': 8.983590, 'e_o_k': [1.104540, 0.883632, 0.706905], 'p_i': 80, 'u_i': 2.2972},
        {'id': 6, 'e_m': 0.387273, 'e_o_k': [0.031492, 0.025193, 0.020155, 0.016124, 0.012899, 0.010319], 'p_i': 10, 'u_i': 1.1140},
        {'id': 7, 'e_m': 6.945788, 'e_o_k': [0.564808, 0.451847, 0.361477, 0.289182, 0.231346, 0.185076], 'p_i': 40, 'u_i': 1.7924},
    ]
    B_BUDGET = 71.760008
    return processors, tasks, B_BUDGET

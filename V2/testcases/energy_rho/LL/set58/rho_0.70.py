"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 49.680001, "H": 80, "J": 40, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.7, "seed": 1058, "set": 58, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}
"""

_SPEC = '{"B": 49.680001, "H": 80, "J": 40, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 0.7, "seed": 1058, "set": 58, "sweep": "energy_rho", "util_per_core": 0.2, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.629540, 'e_o_k': [0.085320, 0.068256, 0.054605, 0.043684, 0.034947, 0.027958], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 1.955326, 'e_o_k': [0.543146, 0.434517], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.277667, 'e_o_k': [0.056899, 0.045519, 0.036415], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 2.558681, 'e_o_k': [0.710745, 0.568596], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 0.415486, 'e_o_k': [0.070374, 0.056299, 0.045039, 0.036031], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 6.998742, 'e_o_k': [1.944095, 1.555276], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 0.663543, 'e_o_k': [0.112389, 0.089911, 0.071929, 0.057543], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.049673, 'e_o_k': [0.008413, 0.006731, 0.005385, 0.004308], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 49.680001
    return processors, tasks, B_BUDGET

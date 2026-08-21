"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440007, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440007, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.243815, 'e_o_k': [0.021759, 0.017407, 0.013926, 0.011141, 0.008912], 'p_i': 10, 'u_i': 1.7922},
        {'id': 1, 'e_m': 5.569559, 'e_o_k': [0.566012, 0.452810, 0.362248, 0.289798], 'p_i': 20, 'u_i': 4.9529},
        {'id': 2, 'e_m': 7.770253, 'e_o_k': [1.295042, 1.036034], 'p_i': 40, 'u_i': 2.3587},
        {'id': 3, 'e_m': 3.069510, 'e_o_k': [0.511585, 0.409268], 'p_i': 80, 'u_i': 4.5300},
        {'id': 4, 'e_m': 1.363540, 'e_o_k': [0.110879, 0.088703, 0.070962, 0.056770, 0.045416, 0.036333], 'p_i': 80, 'u_i': 3.1308},
        {'id': 5, 'e_m': 16.153153, 'e_o_k': [1.313521, 1.050817, 0.840653, 0.672523, 0.538018, 0.430414], 'p_i': 40, 'u_i': 2.3635},
        {'id': 6, 'e_m': 25.801787, 'e_o_k': [3.172351, 2.537881, 2.030305], 'p_i': 80, 'u_i': 1.8340},
        {'id': 7, 'e_m': 1.211199, 'e_o_k': [0.098491, 0.078793, 0.063034, 0.050427, 0.040342, 0.032273], 'p_i': 10, 'u_i': 2.0052},
    ]
    B_BUDGET = 167.440007
    return processors, tasks, B_BUDGET

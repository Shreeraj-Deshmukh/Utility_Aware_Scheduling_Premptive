"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440002, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.134230, 'e_o_k': [0.336182, 0.268946, 0.215156, 0.172125, 0.137700, 0.110160], 'p_i': 10, 'u_i': 4.5134},
        {'id': 1, 'e_m': 3.182151, 'e_o_k': [0.391248, 0.312998, 0.250399], 'p_i': 20, 'u_i': 4.5874},
        {'id': 2, 'e_m': 3.532200, 'e_o_k': [0.434287, 0.347430, 0.277944], 'p_i': 40, 'u_i': 2.7347},
        {'id': 3, 'e_m': 19.210808, 'e_o_k': [2.361985, 1.889588, 1.511670], 'p_i': 80, 'u_i': 4.9671},
        {'id': 4, 'e_m': 9.519994, 'e_o_k': [0.849595, 0.679676, 0.543741, 0.434993, 0.347994], 'p_i': 80, 'u_i': 4.8761},
        {'id': 5, 'e_m': 0.497178, 'e_o_k': [0.050526, 0.040421, 0.032337, 0.025869], 'p_i': 10, 'u_i': 2.5248},
        {'id': 6, 'e_m': 2.547541, 'e_o_k': [0.424590, 0.339672], 'p_i': 40, 'u_i': 4.9532},
        {'id': 7, 'e_m': 10.664925, 'e_o_k': [1.083834, 0.867067, 0.693654, 0.554923], 'p_i': 40, 'u_i': 2.2979},
    ]
    B_BUDGET = 167.440002
    return processors, tasks, B_BUDGET

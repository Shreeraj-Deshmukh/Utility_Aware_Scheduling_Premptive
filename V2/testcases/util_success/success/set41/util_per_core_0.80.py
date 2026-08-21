"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360002, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360002, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1041, "set": 41, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.611841, 'e_o_k': [0.143846, 0.115077, 0.092061, 0.073649, 0.058919], 'p_i': 10, 'u_i': 1.5284},
        {'id': 1, 'e_m': 0.907541, 'e_o_k': [0.092230, 0.073784, 0.059027, 0.047222], 'p_i': 20, 'u_i': 4.7182},
        {'id': 2, 'e_m': 4.287743, 'e_o_k': [0.435746, 0.348597, 0.278878, 0.223102], 'p_i': 40, 'u_i': 3.4247},
        {'id': 3, 'e_m': 20.977555, 'e_o_k': [2.131865, 1.705492, 1.364394, 1.091515], 'p_i': 80, 'u_i': 4.7267},
        {'id': 4, 'e_m': 35.453366, 'e_o_k': [3.602984, 2.882387, 2.305910, 1.844728], 'p_i': 80, 'u_i': 3.5037},
        {'id': 5, 'e_m': 0.161561, 'e_o_k': [0.014418, 0.011535, 0.009228, 0.007382, 0.005906], 'p_i': 10, 'u_i': 1.8182},
        {'id': 6, 'e_m': 15.772339, 'e_o_k': [1.602880, 1.282304, 1.025843, 0.820675], 'p_i': 40, 'u_i': 2.8197},
        {'id': 7, 'e_m': 1.703942, 'e_o_k': [0.173165, 0.138532, 0.110825, 0.088660], 'p_i': 10, 'u_i': 3.0802},
    ]
    B_BUDGET = 191.360002
    return processors, tasks, B_BUDGET

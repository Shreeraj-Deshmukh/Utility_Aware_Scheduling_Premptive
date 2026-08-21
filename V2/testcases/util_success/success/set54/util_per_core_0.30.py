"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759983, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759983, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1054, "set": 54, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.545066, 'e_o_k': [0.189967, 0.151974, 0.121579], 'p_i': 10, 'u_i': 3.7892},
        {'id': 1, 'e_m': 0.254269, 'e_o_k': [0.025840, 0.020672, 0.016538, 0.013230], 'p_i': 20, 'u_i': 2.5683},
        {'id': 2, 'e_m': 11.885395, 'e_o_k': [1.207865, 0.966292, 0.773034, 0.618427], 'p_i': 40, 'u_i': 1.2577},
        {'id': 3, 'e_m': 1.322169, 'e_o_k': [0.117995, 0.094396, 0.075517, 0.060413, 0.048331], 'p_i': 80, 'u_i': 3.4086},
        {'id': 4, 'e_m': 0.588743, 'e_o_k': [0.072386, 0.057909, 0.046327], 'p_i': 40, 'u_i': 3.2935},
        {'id': 5, 'e_m': 0.610820, 'e_o_k': [0.062075, 0.049660, 0.039728, 0.031782], 'p_i': 10, 'u_i': 4.9988},
        {'id': 6, 'e_m': 0.124089, 'e_o_k': [0.011074, 0.008859, 0.007087, 0.005670, 0.004536], 'p_i': 20, 'u_i': 2.8879},
        {'id': 7, 'e_m': 0.742258, 'e_o_k': [0.075433, 0.060346, 0.048277, 0.038622], 'p_i': 20, 'u_i': 4.7528},
    ]
    B_BUDGET = 71.759983
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440001, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1081, "set": 81, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.414033, 'e_o_k': [0.114984, 0.091988, 0.073590, 0.058872, 0.047098, 0.037678], 'p_i': 10, 'u_i': 2.7135},
        {'id': 1, 'e_m': 4.593199, 'e_o_k': [0.373504, 0.298803, 0.239042, 0.191234, 0.152987, 0.122390], 'p_i': 20, 'u_i': 1.9259},
        {'id': 2, 'e_m': 5.309362, 'e_o_k': [0.539569, 0.431655, 0.345324, 0.276259], 'p_i': 40, 'u_i': 2.2208},
        {'id': 3, 'e_m': 35.246735, 'e_o_k': [3.145532, 2.516426, 2.013140, 1.610512, 1.288410], 'p_i': 80, 'u_i': 3.1305},
        {'id': 4, 'e_m': 3.789963, 'e_o_k': [0.465979, 0.372783, 0.298227], 'p_i': 20, 'u_i': 2.6666},
        {'id': 5, 'e_m': 0.238164, 'e_o_k': [0.024204, 0.019363, 0.015490, 0.012392], 'p_i': 20, 'u_i': 4.9673},
        {'id': 6, 'e_m': 6.782667, 'e_o_k': [0.689295, 0.551436, 0.441149, 0.352919], 'p_i': 40, 'u_i': 1.1268},
        {'id': 7, 'e_m': 0.846455, 'e_o_k': [0.086022, 0.068818, 0.055054, 0.044043], 'p_i': 10, 'u_i': 4.3594},
    ]
    B_BUDGET = 167.440001
    return processors, tasks, B_BUDGET

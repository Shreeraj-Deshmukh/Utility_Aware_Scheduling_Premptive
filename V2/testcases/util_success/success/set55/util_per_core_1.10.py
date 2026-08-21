"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120003, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120003, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1055, "set": 55, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.726325, 'e_o_k': [0.287721, 0.230177], 'p_i': 10, 'u_i': 2.5239},
        {'id': 1, 'e_m': 6.694904, 'e_o_k': [1.115817, 0.892654], 'p_i': 20, 'u_i': 1.8339},
        {'id': 2, 'e_m': 8.464545, 'e_o_k': [0.860218, 0.688174, 0.550539, 0.440432], 'p_i': 40, 'u_i': 4.8055},
        {'id': 3, 'e_m': 35.553633, 'e_o_k': [5.925605, 4.740484], 'p_i': 80, 'u_i': 3.2084},
        {'id': 4, 'e_m': 3.313845, 'e_o_k': [0.407440, 0.325952, 0.260762], 'p_i': 20, 'u_i': 1.8854},
        {'id': 5, 'e_m': 4.057375, 'e_o_k': [0.329932, 0.263946, 0.211157, 0.168925, 0.135140, 0.108112], 'p_i': 10, 'u_i': 4.9503},
        {'id': 6, 'e_m': 21.069255, 'e_o_k': [1.880288, 1.504230, 1.203384, 0.962707, 0.770166], 'p_i': 80, 'u_i': 3.0972},
        {'id': 7, 'e_m': 16.143430, 'e_o_k': [1.984848, 1.587878, 1.270303], 'p_i': 80, 'u_i': 2.5144},
    ]
    B_BUDGET = 263.120003
    return processors, tasks, B_BUDGET

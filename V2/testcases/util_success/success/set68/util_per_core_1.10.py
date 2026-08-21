"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120003, "H": 80, "J": 32, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.140962, 'e_o_k': [0.140282, 0.112226, 0.089781], 'p_i': 10, 'u_i': 1.1616},
        {'id': 1, 'e_m': 4.358976, 'e_o_k': [0.535940, 0.428752, 0.343001], 'p_i': 20, 'u_i': 1.7018},
        {'id': 2, 'e_m': 19.265058, 'e_o_k': [2.368655, 1.894924, 1.515939], 'p_i': 40, 'u_i': 3.8642},
        {'id': 3, 'e_m': 19.998462, 'e_o_k': [3.333077, 2.666462], 'p_i': 80, 'u_i': 1.2777},
        {'id': 4, 'e_m': 6.590131, 'e_o_k': [0.669729, 0.535783, 0.428626, 0.342901], 'p_i': 20, 'u_i': 4.6633},
        {'id': 5, 'e_m': 6.327394, 'e_o_k': [0.643028, 0.514422, 0.411538, 0.329230], 'p_i': 20, 'u_i': 1.0039},
        {'id': 6, 'e_m': 0.205150, 'e_o_k': [0.025223, 0.020179, 0.016143], 'p_i': 10, 'u_i': 3.4899},
        {'id': 7, 'e_m': 37.596521, 'e_o_k': [6.266087, 5.012870], 'p_i': 80, 'u_i': 3.2831},
    ]
    B_BUDGET = 263.120003
    return processors, tasks, B_BUDGET

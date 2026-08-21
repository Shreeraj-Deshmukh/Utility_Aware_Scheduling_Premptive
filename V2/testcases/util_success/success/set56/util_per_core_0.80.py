"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360007, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360007, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1056, "set": 56, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.159159, 'e_o_k': [0.117801, 0.094241, 0.075392, 0.060314], 'p_i': 10, 'u_i': 4.6704},
        {'id': 1, 'e_m': 0.149794, 'e_o_k': [0.024966, 0.019973], 'p_i': 20, 'u_i': 1.7142},
        {'id': 2, 'e_m': 14.823432, 'e_o_k': [1.822553, 1.458043, 1.166434], 'p_i': 40, 'u_i': 2.7421},
        {'id': 3, 'e_m': 18.284450, 'e_o_k': [1.486831, 1.189465, 0.951572, 0.761257, 0.609006, 0.487205], 'p_i': 80, 'u_i': 1.9194},
        {'id': 4, 'e_m': 7.575783, 'e_o_k': [1.262631, 1.010104], 'p_i': 20, 'u_i': 4.0448},
        {'id': 5, 'e_m': 6.214013, 'e_o_k': [0.764018, 0.611214, 0.488972], 'p_i': 20, 'u_i': 1.1256},
        {'id': 6, 'e_m': 0.205669, 'e_o_k': [0.020901, 0.016721, 0.013377, 0.010701], 'p_i': 10, 'u_i': 3.9028},
        {'id': 7, 'e_m': 3.347926, 'e_o_k': [0.298780, 0.239024, 0.191219, 0.152975, 0.122380], 'p_i': 20, 'u_i': 2.5194},
    ]
    B_BUDGET = 191.360007
    return processors, tasks, B_BUDGET

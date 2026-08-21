"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359997, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359997, "H": 80, "J": 25, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.328411, 'e_o_k': [0.040378, 0.032303, 0.025842], 'p_i': 10, 'u_i': 1.5400},
        {'id': 1, 'e_m': 2.178863, 'e_o_k': [0.177178, 0.141742, 0.113394, 0.090715, 0.072572, 0.058058], 'p_i': 20, 'u_i': 3.1935},
        {'id': 2, 'e_m': 17.004433, 'e_o_k': [2.834072, 2.267258], 'p_i': 40, 'u_i': 2.6679},
        {'id': 3, 'e_m': 39.496857, 'e_o_k': [6.582809, 5.266248], 'p_i': 80, 'u_i': 2.8390},
        {'id': 4, 'e_m': 3.951331, 'e_o_k': [0.485819, 0.388656, 0.310924], 'p_i': 20, 'u_i': 3.5794},
        {'id': 5, 'e_m': 3.787639, 'e_o_k': [0.384923, 0.307938, 0.246351, 0.197080], 'p_i': 80, 'u_i': 4.0478},
        {'id': 6, 'e_m': 11.005802, 'e_o_k': [0.894955, 0.715964, 0.572771, 0.458217, 0.366574, 0.293259], 'p_i': 80, 'u_i': 1.4500},
        {'id': 7, 'e_m': 3.138193, 'e_o_k': [0.385843, 0.308675, 0.246940], 'p_i': 20, 'u_i': 4.5142},
    ]
    B_BUDGET = 191.359997
    return processors, tasks, B_BUDGET

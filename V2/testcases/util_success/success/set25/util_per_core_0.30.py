"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.76, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.76, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.199580, 'e_o_k': [0.199930, 0.159944], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 3.889142, 'e_o_k': [0.478173, 0.382539, 0.306031], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 2.191668, 'e_o_k': [0.222731, 0.178184, 0.142548, 0.114038], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 5.688368, 'e_o_k': [0.948061, 0.758449], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 0.779240, 'e_o_k': [0.063365, 0.050692, 0.040554, 0.032443, 0.025954, 0.020764], 'p_i': 40, 'u_i': 4.9580},
        {'id': 5, 'e_m': 1.066268, 'e_o_k': [0.086705, 0.069364, 0.055491, 0.044393, 0.035515, 0.028412], 'p_i': 20, 'u_i': 2.0799},
        {'id': 6, 'e_m': 2.377340, 'e_o_k': [0.396223, 0.316979], 'p_i': 40, 'u_i': 1.2465},
        {'id': 7, 'e_m': 0.274607, 'e_o_k': [0.033763, 0.027011, 0.021608], 'p_i': 10, 'u_i': 3.7304},
    ]
    B_BUDGET = 71.760000
    return processors, tasks, B_BUDGET

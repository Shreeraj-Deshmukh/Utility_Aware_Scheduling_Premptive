"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.360001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.360001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.588050, 'e_o_k': [0.129135, 0.103308, 0.082646, 0.066117, 0.052894, 0.042315], 'p_i': 10, 'u_i': 1.8568},
        {'id': 1, 'e_m': 7.341286, 'e_o_k': [0.902617, 0.722094, 0.577675], 'p_i': 20, 'u_i': 1.8128},
        {'id': 2, 'e_m': 3.839673, 'e_o_k': [0.639945, 0.511956], 'p_i': 40, 'u_i': 1.5689},
        {'id': 3, 'e_m': 5.733032, 'e_o_k': [0.582625, 0.466100, 0.372880, 0.298304], 'p_i': 80, 'u_i': 4.8976},
        {'id': 4, 'e_m': 1.523653, 'e_o_k': [0.123898, 0.099119, 0.079295, 0.063436, 0.050749, 0.040599], 'p_i': 40, 'u_i': 2.5447},
        {'id': 5, 'e_m': 16.334224, 'e_o_k': [2.722371, 2.177897], 'p_i': 40, 'u_i': 1.6969},
        {'id': 6, 'e_m': 4.648745, 'e_o_k': [0.472433, 0.377947, 0.302357, 0.241886], 'p_i': 80, 'u_i': 4.6966},
        {'id': 7, 'e_m': 32.153580, 'e_o_k': [2.869489, 2.295591, 1.836473, 1.469178, 1.175343], 'p_i': 80, 'u_i': 4.2096},
    ]
    B_BUDGET = 191.360001
    return processors, tasks, B_BUDGET

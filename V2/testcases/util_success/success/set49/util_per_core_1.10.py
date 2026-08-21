"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120001, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.428015, 'e_o_k': [0.298526, 0.238821, 0.191057], 'p_i': 10, 'u_i': 2.1584},
        {'id': 1, 'e_m': 1.573240, 'e_o_k': [0.262207, 0.209765], 'p_i': 20, 'u_i': 3.1132},
        {'id': 2, 'e_m': 9.805731, 'e_o_k': [0.996517, 0.797214, 0.637771, 0.510217], 'p_i': 40, 'u_i': 2.8815},
        {'id': 3, 'e_m': 26.864326, 'e_o_k': [2.730114, 2.184092, 1.747273, 1.397819], 'p_i': 80, 'u_i': 4.0072},
        {'id': 4, 'e_m': 14.926990, 'e_o_k': [2.487832, 1.990265], 'p_i': 40, 'u_i': 2.4398},
        {'id': 5, 'e_m': 32.008449, 'e_o_k': [2.602821, 2.082257, 1.665805, 1.332644, 1.066115, 0.852892], 'p_i': 80, 'u_i': 1.4034},
        {'id': 6, 'e_m': 4.210232, 'e_o_k': [0.427869, 0.342295, 0.273836, 0.219069], 'p_i': 10, 'u_i': 2.1565},
        {'id': 7, 'e_m': 4.131428, 'e_o_k': [0.368702, 0.294962, 0.235969, 0.188775, 0.151020], 'p_i': 40, 'u_i': 3.4806},
    ]
    B_BUDGET = 263.120001
    return processors, tasks, B_BUDGET

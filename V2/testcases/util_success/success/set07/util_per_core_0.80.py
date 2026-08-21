"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 191.359974, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}
"""

_SPEC = '{"B": 191.359974, "H": 80, "J": 33, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "util_success", "util_per_core": 0.8, "value": "0.80"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.028723, 'e_o_k': [0.164969, 0.131975, 0.105580, 0.084464, 0.067571, 0.054057], 'p_i': 10, 'u_i': 3.5703},
        {'id': 1, 'e_m': 6.262621, 'e_o_k': [0.636445, 0.509156, 0.407325, 0.325860], 'p_i': 20, 'u_i': 4.1664},
        {'id': 2, 'e_m': 1.157175, 'e_o_k': [0.094098, 0.075278, 0.060222, 0.048178, 0.038542, 0.030834], 'p_i': 40, 'u_i': 1.4904},
        {'id': 3, 'e_m': 22.614539, 'e_o_k': [2.018194, 1.614555, 1.291644, 1.033315, 0.826652], 'p_i': 80, 'u_i': 4.1413},
        {'id': 4, 'e_m': 4.182385, 'e_o_k': [0.425039, 0.340031, 0.272025, 0.217620], 'p_i': 10, 'u_i': 2.8602},
        {'id': 5, 'e_m': 0.928986, 'e_o_k': [0.114220, 0.091376, 0.073101], 'p_i': 20, 'u_i': 3.3364},
        {'id': 6, 'e_m': 1.937432, 'e_o_k': [0.322905, 0.258324], 'p_i': 20, 'u_i': 2.1410},
        {'id': 7, 'e_m': 8.433041, 'e_o_k': [0.685747, 0.548598, 0.438878, 0.351102, 0.280882, 0.224706], 'p_i': 40, 'u_i': 4.3280},
    ]
    B_BUDGET = 191.359974
    return processors, tasks, B_BUDGET

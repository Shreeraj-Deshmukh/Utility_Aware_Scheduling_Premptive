"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 37, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "freq", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 37, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "freq", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.000930, 'e_o_k': [0.000258, 0.000207], 'p_i': 10, 'u_i': 1.4564},
        {'id': 1, 'e_m': 0.515106, 'e_o_k': [0.087247, 0.069798, 0.055838, 0.044670], 'p_i': 20, 'u_i': 1.4719},
        {'id': 2, 'e_m': 0.249987, 'e_o_k': [0.051227, 0.040981, 0.032785], 'p_i': 40, 'u_i': 1.0831},
        {'id': 3, 'e_m': 1.651906, 'e_o_k': [0.245702, 0.196562, 0.157250, 0.125800, 0.100640], 'p_i': 80, 'u_i': 3.5025},
        {'id': 4, 'e_m': 8.382844, 'e_o_k': [1.136108, 0.908887, 0.727109, 0.581688, 0.465350, 0.372280], 'p_i': 40, 'u_i': 3.4020},
        {'id': 5, 'e_m': 0.849274, 'e_o_k': [0.235910, 0.188728], 'p_i': 20, 'u_i': 4.4776},
        {'id': 6, 'e_m': 0.094741, 'e_o_k': [0.012840, 0.010272, 0.008218, 0.006574, 0.005259, 0.004207], 'p_i': 10, 'u_i': 3.0661},
        {'id': 7, 'e_m': 0.857443, 'e_o_k': [0.116207, 0.092966, 0.074373, 0.059498, 0.047599, 0.038079], 'p_i': 10, 'u_i': 2.9486},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET

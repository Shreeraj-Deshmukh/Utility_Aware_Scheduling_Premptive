"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279982, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279982, "H": 80, "J": 27, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.018283, 'e_o_k': [0.371100, 0.296880, 0.237504], 'p_i': 10, 'u_i': 3.1129},
        {'id': 1, 'e_m': 6.351333, 'e_o_k': [0.566813, 0.453451, 0.362761, 0.290208, 0.232167], 'p_i': 20, 'u_i': 1.3211},
        {'id': 2, 'e_m': 16.074776, 'e_o_k': [2.679129, 2.143303], 'p_i': 40, 'u_i': 4.8977},
        {'id': 3, 'e_m': 19.646139, 'e_o_k': [3.274356, 2.619485], 'p_i': 80, 'u_i': 2.1715},
        {'id': 4, 'e_m': 6.440886, 'e_o_k': [0.791912, 0.633530, 0.506824], 'p_i': 20, 'u_i': 1.5264},
        {'id': 5, 'e_m': 0.283314, 'e_o_k': [0.047219, 0.037775], 'p_i': 40, 'u_i': 1.6618},
        {'id': 6, 'e_m': 1.530830, 'e_o_k': [0.136616, 0.109293, 0.087434, 0.069947, 0.055958], 'p_i': 20, 'u_i': 4.2147},
        {'id': 7, 'e_m': 5.099609, 'e_o_k': [0.849935, 0.679948], 'p_i': 40, 'u_i': 3.7475},
    ]
    B_BUDGET = 215.279982
    return processors, tasks, B_BUDGET

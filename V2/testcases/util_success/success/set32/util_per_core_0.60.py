"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519999, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519999, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.522924, 'e_o_k': [0.135911, 0.108729, 0.086983, 0.069586, 0.055669], 'p_i': 10, 'u_i': 2.6437},
        {'id': 1, 'e_m': 2.007206, 'e_o_k': [0.163219, 0.130575, 0.104460, 0.083568, 0.066855, 0.053484], 'p_i': 20, 'u_i': 2.4707},
        {'id': 2, 'e_m': 1.823054, 'e_o_k': [0.148245, 0.118596, 0.094877, 0.075901, 0.060721, 0.048577], 'p_i': 40, 'u_i': 1.1046},
        {'id': 3, 'e_m': 17.141210, 'e_o_k': [2.856868, 2.285495], 'p_i': 80, 'u_i': 3.2848},
        {'id': 4, 'e_m': 6.289125, 'e_o_k': [0.639139, 0.511311, 0.409049, 0.327239], 'p_i': 40, 'u_i': 2.0063},
        {'id': 5, 'e_m': 0.811572, 'e_o_k': [0.082477, 0.065981, 0.052785, 0.042228], 'p_i': 10, 'u_i': 1.2869},
        {'id': 6, 'e_m': 8.491052, 'e_o_k': [1.415175, 1.132140], 'p_i': 20, 'u_i': 2.7193},
        {'id': 7, 'e_m': 0.982716, 'e_o_k': [0.163786, 0.131029], 'p_i': 40, 'u_i': 1.9085},
    ]
    B_BUDGET = 143.519999
    return processors, tasks, B_BUDGET

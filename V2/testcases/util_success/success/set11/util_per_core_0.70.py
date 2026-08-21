"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 167.440005, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}
"""

_SPEC = '{"B": 167.440005, "H": 80, "J": 30, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "util_success", "util_per_core": 0.7, "value": "0.70"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.055703, 'e_o_k': [0.272701, 0.218161, 0.174529, 0.139623, 0.111698], 'p_i': 10, 'u_i': 4.9659},
        {'id': 1, 'e_m': 2.620556, 'e_o_k': [0.233867, 0.187093, 0.149675, 0.119740, 0.095792], 'p_i': 20, 'u_i': 4.3569},
        {'id': 2, 'e_m': 8.315355, 'e_o_k': [1.022380, 0.817904, 0.654323], 'p_i': 40, 'u_i': 3.1411},
        {'id': 3, 'e_m': 3.347904, 'e_o_k': [0.340234, 0.272187, 0.217750, 0.174200], 'p_i': 80, 'u_i': 3.1206},
        {'id': 4, 'e_m': 3.936244, 'e_o_k': [0.483964, 0.387172, 0.309737], 'p_i': 20, 'u_i': 4.7030},
        {'id': 5, 'e_m': 1.107128, 'e_o_k': [0.184521, 0.147617], 'p_i': 10, 'u_i': 2.0532},
        {'id': 6, 'e_m': 28.822455, 'e_o_k': [2.572209, 2.057767, 1.646214, 1.316971, 1.053577], 'p_i': 80, 'u_i': 1.9357},
        {'id': 7, 'e_m': 1.834540, 'e_o_k': [0.163720, 0.130976, 0.104781, 0.083825, 0.067060], 'p_i': 40, 'u_i': 4.8494},
    ]
    B_BUDGET = 167.440005
    return processors, tasks, B_BUDGET

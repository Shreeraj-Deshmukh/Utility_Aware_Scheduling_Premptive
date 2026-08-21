"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.760001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.760001, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.054325, 'e_o_k': [0.004418, 0.003534, 0.002827, 0.002262, 0.001809, 0.001448], 'p_i': 10, 'u_i': 2.1441},
        {'id': 1, 'e_m': 0.861126, 'e_o_k': [0.076850, 0.061480, 0.049184, 0.039347, 0.031478], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 7.567468, 'e_o_k': [0.769052, 0.615241, 0.492193, 0.393754], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 11.725836, 'e_o_k': [1.441701, 1.153361, 0.922689], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 3.980844, 'e_o_k': [0.663474, 0.530779], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 3.246272, 'e_o_k': [0.399132, 0.319305, 0.255444], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 3.497644, 'e_o_k': [0.355452, 0.284361, 0.227489, 0.181991], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 1.644544, 'e_o_k': [0.146764, 0.117412, 0.093929, 0.075143, 0.060115], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 71.760001
    return processors, tasks, B_BUDGET

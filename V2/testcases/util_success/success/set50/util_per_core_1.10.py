"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120005, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120005, "H": 80, "J": 35, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.922827, 'e_o_k': [0.113462, 0.090770, 0.072616], 'p_i': 10, 'u_i': 4.6385},
        {'id': 1, 'e_m': 6.614374, 'e_o_k': [0.537859, 0.430287, 0.344230, 0.275384, 0.220307, 0.176246], 'p_i': 20, 'u_i': 4.0834},
        {'id': 2, 'e_m': 18.867399, 'e_o_k': [3.144566, 2.515653], 'p_i': 40, 'u_i': 3.3121},
        {'id': 3, 'e_m': 9.788434, 'e_o_k': [1.203496, 0.962797, 0.770237], 'p_i': 80, 'u_i': 3.8703},
        {'id': 4, 'e_m': 7.436963, 'e_o_k': [0.663699, 0.530959, 0.424767, 0.339814, 0.271851], 'p_i': 20, 'u_i': 3.8303},
        {'id': 5, 'e_m': 6.846370, 'e_o_k': [0.841767, 0.673413, 0.538731], 'p_i': 20, 'u_i': 2.8745},
        {'id': 6, 'e_m': 8.880451, 'e_o_k': [0.722129, 0.577703, 0.462162, 0.369730, 0.295784, 0.236627], 'p_i': 20, 'u_i': 1.9044},
        {'id': 7, 'e_m': 0.247689, 'e_o_k': [0.022105, 0.017684, 0.014147, 0.011318, 0.009054], 'p_i': 10, 'u_i': 4.6877},
    ]
    B_BUDGET = 263.120005
    return processors, tasks, B_BUDGET

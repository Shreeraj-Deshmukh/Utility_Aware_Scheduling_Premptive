"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519995, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519995, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.108651, 'e_o_k': [0.008835, 0.007068, 0.005654, 0.004524, 0.003619, 0.002895], 'p_i': 10, 'u_i': 2.1441},
        {'id': 1, 'e_m': 1.722252, 'e_o_k': [0.153699, 0.122959, 0.098368, 0.078694, 0.062955], 'p_i': 20, 'u_i': 1.5180},
        {'id': 2, 'e_m': 15.134935, 'e_o_k': [1.538103, 1.230483, 0.984386, 0.787509], 'p_i': 40, 'u_i': 2.4726},
        {'id': 3, 'e_m': 23.451671, 'e_o_k': [2.883402, 2.306722, 1.845377], 'p_i': 80, 'u_i': 4.1932},
        {'id': 4, 'e_m': 7.961689, 'e_o_k': [1.326948, 1.061559], 'p_i': 80, 'u_i': 2.7154},
        {'id': 5, 'e_m': 6.492544, 'e_o_k': [0.798264, 0.638611, 0.510889], 'p_i': 40, 'u_i': 4.3253},
        {'id': 6, 'e_m': 6.995288, 'e_o_k': [0.710903, 0.568723, 0.454978, 0.363982], 'p_i': 80, 'u_i': 1.0005},
        {'id': 7, 'e_m': 3.289089, 'e_o_k': [0.293529, 0.234823, 0.187858, 0.150287, 0.120229], 'p_i': 40, 'u_i': 1.9051},
    ]
    B_BUDGET = 143.519995
    return processors, tasks, B_BUDGET

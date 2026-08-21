"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 263.120002, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}
"""

_SPEC = '{"B": 263.120002, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1052, "set": 52, "sweep": "util_success", "util_per_core": 1.1, "value": "1.10"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.258258, 'e_o_k': [0.277655, 0.222124, 0.177699], 'p_i': 10, 'u_i': 4.1932},
        {'id': 1, 'e_m': 3.073535, 'e_o_k': [0.512256, 0.409805], 'p_i': 20, 'u_i': 2.7154},
        {'id': 2, 'e_m': 1.743396, 'e_o_k': [0.214352, 0.171482, 0.137185], 'p_i': 40, 'u_i': 4.3253},
        {'id': 3, 'e_m': 37.444019, 'e_o_k': [3.805286, 3.044229, 2.435383, 1.948307], 'p_i': 80, 'u_i': 1.0005},
        {'id': 4, 'e_m': 8.946927, 'e_o_k': [0.798453, 0.638762, 0.511010, 0.408808, 0.327046], 'p_i': 80, 'u_i': 1.9051},
        {'id': 5, 'e_m': 6.714192, 'e_o_k': [0.599196, 0.479357, 0.383486, 0.306788, 0.245431], 'p_i': 20, 'u_i': 2.2450},
        {'id': 6, 'e_m': 19.384136, 'e_o_k': [3.230689, 2.584551], 'p_i': 40, 'u_i': 3.5907},
        {'id': 7, 'e_m': 15.068507, 'e_o_k': [1.852685, 1.482148, 1.185719], 'p_i': 40, 'u_i': 4.3441},
    ]
    B_BUDGET = 263.120002
    return processors, tasks, B_BUDGET

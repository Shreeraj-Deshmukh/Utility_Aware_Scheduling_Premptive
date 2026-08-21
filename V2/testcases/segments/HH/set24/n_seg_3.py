"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 30, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1024, "set": 24, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.255086, 'e_o_k': [0.146361, 0.117088, 0.093671], 'p_i': 10, 'u_i': 1.4092},
        {'id': 1, 'e_m': 1.766930, 'e_o_k': [1.013812, 0.811050, 0.648840], 'p_i': 20, 'u_i': 2.7448},
        {'id': 2, 'e_m': 4.717796, 'e_o_k': [2.706932, 2.165546, 1.732437], 'p_i': 40, 'u_i': 3.9391},
        {'id': 3, 'e_m': 2.076602, 'e_o_k': [1.191493, 0.953195, 0.762556], 'p_i': 80, 'u_i': 3.4662},
        {'id': 4, 'e_m': 0.980401, 'e_o_k': [0.562525, 0.450020, 0.360016], 'p_i': 40, 'u_i': 1.1407},
        {'id': 5, 'e_m': 28.292425, 'e_o_k': [16.233358, 12.986687, 10.389349], 'p_i': 80, 'u_i': 3.5457},
        {'id': 6, 'e_m': 0.799254, 'e_o_k': [0.458588, 0.366871, 0.293496], 'p_i': 10, 'u_i': 1.4096},
        {'id': 7, 'e_m': 1.683036, 'e_o_k': [0.965676, 0.772541, 0.618033], 'p_i': 20, 'u_i': 4.8654},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET

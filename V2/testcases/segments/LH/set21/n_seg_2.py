"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.345721, 'e_o_k': [0.268894, 0.215115], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 1.825589, 'e_o_k': [1.419902, 1.135922], 'p_i': 20, 'u_i': 2.2851},
        {'id': 2, 'e_m': 2.684855, 'e_o_k': [2.088220, 1.670576], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 4.826850, 'e_o_k': [3.754217, 3.003374], 'p_i': 80, 'u_i': 2.3867},
        {'id': 4, 'e_m': 0.378406, 'e_o_k': [0.294316, 0.235453], 'p_i': 10, 'u_i': 1.9527},
        {'id': 5, 'e_m': 0.374820, 'e_o_k': [0.291527, 0.233221], 'p_i': 10, 'u_i': 2.5555},
        {'id': 6, 'e_m': 3.374313, 'e_o_k': [2.624466, 2.099573], 'p_i': 80, 'u_i': 2.5749},
        {'id': 7, 'e_m': 1.167596, 'e_o_k': [0.908130, 0.726504], 'p_i': 40, 'u_i': 4.5972},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET

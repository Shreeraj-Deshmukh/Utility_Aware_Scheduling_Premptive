"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.962850, 'e_o_k': [0.291952, 0.233561, 0.186849, 0.149479, 0.119583], 'p_i': 10, 'u_i': 2.5478},
        {'id': 1, 'e_m': 1.302586, 'e_o_k': [0.220628, 0.176502, 0.141202, 0.112961], 'p_i': 20, 'u_i': 1.9017},
        {'id': 2, 'e_m': 0.446219, 'e_o_k': [0.123950, 0.099160], 'p_i': 40, 'u_i': 4.1004},
        {'id': 3, 'e_m': 3.381996, 'e_o_k': [0.572831, 0.458265, 0.366612, 0.293290], 'p_i': 80, 'u_i': 2.6358},
        {'id': 4, 'e_m': 0.023935, 'e_o_k': [0.004905, 0.003924, 0.003139], 'p_i': 20, 'u_i': 4.3577},
        {'id': 5, 'e_m': 3.358343, 'e_o_k': [0.568825, 0.455060, 0.364048, 0.291238], 'p_i': 40, 'u_i': 4.2383},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1030, "set": 30, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.056959, 'e_o_k': [0.011672, 0.009338, 0.007470], 'p_i': 10, 'u_i': 4.7642},
        {'id': 1, 'e_m': 2.740391, 'e_o_k': [0.407602, 0.326082, 0.260865, 0.208692, 0.166954], 'p_i': 20, 'u_i': 4.7668},
        {'id': 2, 'e_m': 4.138949, 'e_o_k': [0.560943, 0.448754, 0.359003, 0.287203, 0.229762, 0.183810], 'p_i': 40, 'u_i': 4.7724},
        {'id': 3, 'e_m': 12.304866, 'e_o_k': [1.830210, 1.464168, 1.171334, 0.937067, 0.749654], 'p_i': 80, 'u_i': 4.0150},
    ]
    B_BUDGET = 55.200003
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200007, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.200007, "H": 80, "J": 23, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.560596, 'e_o_k': [0.114876, 0.091901, 0.073521], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 2.273229, 'e_o_k': [0.465826, 0.372661, 0.298128], 'p_i': 20, 'u_i': 4.6519},
        {'id': 2, 'e_m': 5.286614, 'e_o_k': [1.083323, 0.866658, 0.693326], 'p_i': 40, 'u_i': 4.9020},
        {'id': 3, 'e_m': 1.840129, 'e_o_k': [0.377076, 0.301661, 0.241328], 'p_i': 80, 'u_i': 4.4826},
        {'id': 4, 'e_m': 0.311968, 'e_o_k': [0.063928, 0.051142, 0.040914], 'p_i': 80, 'u_i': 1.3844},
        {'id': 5, 'e_m': 1.580366, 'e_o_k': [0.323846, 0.259076, 0.207261], 'p_i': 40, 'u_i': 3.8571},
        {'id': 6, 'e_m': 2.375437, 'e_o_k': [0.486770, 0.389416, 0.311533], 'p_i': 80, 'u_i': 3.6185},
        {'id': 7, 'e_m': 0.040206, 'e_o_k': [0.008239, 0.006591, 0.005273], 'p_i': 20, 'u_i': 1.1495},
    ]
    B_BUDGET = 55.200007
    return processors, tasks, B_BUDGET

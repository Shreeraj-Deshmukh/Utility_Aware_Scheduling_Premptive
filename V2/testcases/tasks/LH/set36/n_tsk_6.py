"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1036, "set": 36, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.643703, 'e_o_k': [0.369338, 0.295470, 0.236376], 'p_i': 10, 'u_i': 1.0054},
        {'id': 1, 'e_m': 0.506012, 'e_o_k': [0.239979, 0.191983, 0.153586, 0.122869], 'p_i': 20, 'u_i': 3.4815},
        {'id': 2, 'e_m': 0.577286, 'e_o_k': [0.449000, 0.359200], 'p_i': 40, 'u_i': 3.3828},
        {'id': 3, 'e_m': 3.591706, 'e_o_k': [1.703384, 1.362707, 1.090165, 0.872132], 'p_i': 80, 'u_i': 4.2011},
        {'id': 4, 'e_m': 9.654735, 'e_o_k': [4.578804, 3.663043, 2.930435, 2.344348], 'p_i': 40, 'u_i': 4.7650},
        {'id': 5, 'e_m': 0.770579, 'e_o_k': [0.442136, 0.353708, 0.282967], 'p_i': 80, 'u_i': 4.1252},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 31, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1025, "set": 25, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.599440, 'e_o_k': [0.327754, 0.262203, 0.209763], 'p_i': 10, 'u_i': 2.3541},
        {'id': 1, 'e_m': 5.185523, 'e_o_k': [1.062607, 0.850086, 0.680069], 'p_i': 20, 'u_i': 4.5958},
        {'id': 2, 'e_m': 2.922224, 'e_o_k': [0.598816, 0.479053, 0.383243], 'p_i': 40, 'u_i': 4.0042},
        {'id': 3, 'e_m': 7.584490, 'e_o_k': [1.554199, 1.243359, 0.994687], 'p_i': 80, 'u_i': 1.4529},
        {'id': 4, 'e_m': 1.038987, 'e_o_k': [0.212907, 0.170326, 0.136261], 'p_i': 40, 'u_i': 3.3706},
        {'id': 5, 'e_m': 1.421690, 'e_o_k': [0.291330, 0.233064, 0.186451], 'p_i': 20, 'u_i': 1.2465},
        {'id': 6, 'e_m': 3.169787, 'e_o_k': [0.649546, 0.519637, 0.415710], 'p_i': 40, 'u_i': 3.7304},
        {'id': 7, 'e_m': 0.366143, 'e_o_k': [0.075029, 0.060023, 0.048019], 'p_i': 10, 'u_i': 3.6440},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET

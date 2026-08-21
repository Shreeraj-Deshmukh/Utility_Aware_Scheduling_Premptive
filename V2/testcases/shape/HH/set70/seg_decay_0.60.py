"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639992, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.639992, "H": 80, "J": 23, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1070, "set": 70, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.121191, 'e_o_k': [0.981042, 0.588625], 'p_i': 10, 'u_i': 2.9208},
        {'id': 1, 'e_m': 4.546458, 'e_o_k': [2.670617, 1.602370, 0.961422, 0.576853, 0.346112, 0.207667], 'p_i': 20, 'u_i': 4.6964},
        {'id': 2, 'e_m': 10.573229, 'e_o_k': [7.552306, 4.531384, 2.718830], 'p_i': 40, 'u_i': 4.6519},
        {'id': 3, 'e_m': 3.680258, 'e_o_k': [3.220226, 1.932136], 'p_i': 80, 'u_i': 4.9020},
        {'id': 4, 'e_m': 0.623936, 'e_o_k': [0.366504, 0.219902, 0.131941, 0.079165, 0.047499, 0.028499], 'p_i': 80, 'u_i': 1.1409},
        {'id': 5, 'e_m': 3.160733, 'e_o_k': [1.919251, 1.151551, 0.690930, 0.414558, 0.248735], 'p_i': 40, 'u_i': 1.3844},
        {'id': 6, 'e_m': 4.750875, 'e_o_k': [2.884813, 1.730888, 1.038533, 0.623120, 0.373872], 'p_i': 80, 'u_i': 3.8571},
        {'id': 7, 'e_m': 0.080412, 'e_o_k': [0.070360, 0.042216], 'p_i': 20, 'u_i': 3.6185},
    ]
    B_BUDGET = 176.639992
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199987, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199987, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.490613, 'e_o_k': [0.066492, 0.053193, 0.042555, 0.034044, 0.027235, 0.021788], 'p_i': 10, 'u_i': 4.9438},
        {'id': 1, 'e_m': 0.074164, 'e_o_k': [0.010051, 0.008041, 0.006433, 0.005146, 0.004117, 0.003294], 'p_i': 20, 'u_i': 2.3791},
        {'id': 2, 'e_m': 4.192385, 'e_o_k': [1.164551, 0.931641], 'p_i': 40, 'u_i': 3.1569},
        {'id': 3, 'e_m': 3.073173, 'e_o_k': [0.520524, 0.416419, 0.333135, 0.266508], 'p_i': 80, 'u_i': 2.0315},
        {'id': 4, 'e_m': 0.152558, 'e_o_k': [0.022691, 0.018153, 0.014522, 0.011618, 0.009294], 'p_i': 10, 'u_i': 1.5871},
        {'id': 5, 'e_m': 3.775007, 'e_o_k': [1.048613, 0.838891], 'p_i': 20, 'u_i': 1.8711},
    ]
    B_BUDGET = 55.199987
    return processors, tasks, B_BUDGET

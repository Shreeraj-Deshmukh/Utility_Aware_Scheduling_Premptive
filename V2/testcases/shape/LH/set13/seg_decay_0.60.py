"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319985, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319985, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1013, "set": 13, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.056307, 'e_o_k': [0.040219, 0.024132, 0.014479], 'p_i': 10, 'u_i': 4.5768},
        {'id': 1, 'e_m': 0.343444, 'e_o_k': [0.300514, 0.180308], 'p_i': 20, 'u_i': 3.5463},
        {'id': 2, 'e_m': 1.086388, 'e_o_k': [0.950589, 0.570354], 'p_i': 40, 'u_i': 3.4252},
        {'id': 3, 'e_m': 2.157450, 'e_o_k': [1.388065, 0.832839, 0.499703, 0.299822], 'p_i': 80, 'u_i': 1.2792},
        {'id': 4, 'e_m': 0.190372, 'e_o_k': [0.122482, 0.073489, 0.044094, 0.026456], 'p_i': 10, 'u_i': 2.1862},
        {'id': 5, 'e_m': 4.007311, 'e_o_k': [2.862365, 1.717419, 1.030451], 'p_i': 80, 'u_i': 2.5645},
        {'id': 6, 'e_m': 1.096980, 'e_o_k': [0.705778, 0.423467, 0.254080, 0.152448], 'p_i': 10, 'u_i': 2.2998},
        {'id': 7, 'e_m': 11.539405, 'e_o_k': [8.242432, 4.945459, 2.967276], 'p_i': 80, 'u_i': 1.4896},
    ]
    B_BUDGET = 88.319985
    return processors, tasks, B_BUDGET

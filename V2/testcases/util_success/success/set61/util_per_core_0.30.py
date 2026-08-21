"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 71.759994, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}
"""

_SPEC = '{"B": 71.759994, "H": 80, "J": 21, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "util_success", "util_per_core": 0.3, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.514434, 'e_o_k': [0.052280, 0.041824, 0.033459, 0.026767], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 1.863307, 'e_o_k': [0.189360, 0.151488, 0.121191, 0.096953], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.036053, 'e_o_k': [0.003217, 0.002574, 0.002059, 0.001647, 0.001318], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 8.491010, 'e_o_k': [0.862908, 0.690326, 0.552261, 0.441809], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 7.397235, 'e_o_k': [1.232872, 0.986298], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 2.405372, 'e_o_k': [0.214663, 0.171731, 0.137384, 0.109908, 0.087926], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 7.205290, 'e_o_k': [0.643023, 0.514419, 0.411535, 0.329228, 0.263382], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 1.057678, 'e_o_k': [0.107488, 0.085990, 0.068792, 0.055034], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 71.759994
    return processors, tasks, B_BUDGET

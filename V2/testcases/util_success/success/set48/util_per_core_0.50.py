"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599988, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599988, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.715014, 'e_o_k': [0.285836, 0.228669], 'p_i': 10, 'u_i': 2.6470},
        {'id': 1, 'e_m': 4.360415, 'e_o_k': [0.536117, 0.428893, 0.343115], 'p_i': 20, 'u_i': 4.9479},
        {'id': 2, 'e_m': 0.119955, 'e_o_k': [0.014749, 0.011799, 0.009439], 'p_i': 40, 'u_i': 2.1346},
        {'id': 3, 'e_m': 4.824411, 'e_o_k': [0.804069, 0.643255], 'p_i': 80, 'u_i': 1.3827},
        {'id': 4, 'e_m': 14.547157, 'e_o_k': [2.424526, 1.939621], 'p_i': 80, 'u_i': 3.9576},
        {'id': 5, 'e_m': 2.731567, 'e_o_k': [0.243774, 0.195019, 0.156015, 0.124812, 0.099850], 'p_i': 20, 'u_i': 4.9670},
        {'id': 6, 'e_m': 2.105190, 'e_o_k': [0.187874, 0.150299, 0.120239, 0.096191, 0.076953], 'p_i': 10, 'u_i': 4.5958},
        {'id': 7, 'e_m': 1.458953, 'e_o_k': [0.130202, 0.104161, 0.083329, 0.066663, 0.053331], 'p_i': 80, 'u_i': 1.9552},
    ]
    B_BUDGET = 119.599988
    return processors, tasks, B_BUDGET

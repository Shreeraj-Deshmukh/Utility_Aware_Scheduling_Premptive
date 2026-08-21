"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1045, "set": 45, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.132920, 'e_o_k': [0.019770, 0.015816, 0.012653, 0.010122, 0.008098], 'p_i': 10, 'u_i': 4.9998},
        {'id': 1, 'e_m': 1.465834, 'e_o_k': [0.407176, 0.325741], 'p_i': 20, 'u_i': 2.8601},
        {'id': 2, 'e_m': 0.036091, 'e_o_k': [0.006113, 0.004890, 0.003912, 0.003130], 'p_i': 40, 'u_i': 4.7969},
        {'id': 3, 'e_m': 4.215245, 'e_o_k': [0.626970, 0.501576, 0.401261, 0.321009, 0.256807], 'p_i': 80, 'u_i': 4.3760},
        {'id': 4, 'e_m': 15.724840, 'e_o_k': [3.222303, 2.577843, 2.062274], 'p_i': 80, 'u_i': 3.1042},
        {'id': 5, 'e_m': 37.061042, 'e_o_k': [5.022801, 4.018241, 3.214593, 2.571674, 2.057339, 1.645872], 'p_i': 80, 'u_i': 1.7042},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET

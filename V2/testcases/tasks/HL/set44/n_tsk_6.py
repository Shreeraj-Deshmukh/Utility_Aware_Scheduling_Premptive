"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399985, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399985, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.353209, 'e_o_k': [0.072379, 0.057903, 0.046322], 'p_i': 10, 'u_i': 4.9794},
        {'id': 1, 'e_m': 3.472957, 'e_o_k': [0.470682, 0.376546, 0.301237, 0.240989, 0.192791, 0.154233], 'p_i': 20, 'u_i': 1.8563},
        {'id': 2, 'e_m': 2.131727, 'e_o_k': [0.288908, 0.231127, 0.184901, 0.147921, 0.118337, 0.094669], 'p_i': 40, 'u_i': 1.0975},
        {'id': 3, 'e_m': 14.279303, 'e_o_k': [2.418581, 1.934865, 1.547892, 1.238314], 'p_i': 80, 'u_i': 4.1970},
        {'id': 4, 'e_m': 0.921014, 'e_o_k': [0.124823, 0.099858, 0.079887, 0.063909, 0.051127, 0.040902], 'p_i': 10, 'u_i': 1.7417},
        {'id': 5, 'e_m': 5.342908, 'e_o_k': [0.794697, 0.635758, 0.508606, 0.406885, 0.325508], 'p_i': 20, 'u_i': 3.7063},
    ]
    B_BUDGET = 110.399985
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.274652, 'e_o_k': [0.076292, 0.061034], 'p_i': 10, 'u_i': 1.3629},
        {'id': 1, 'e_m': 7.567318, 'e_o_k': [1.281727, 1.025382, 0.820305, 0.656244], 'p_i': 20, 'u_i': 1.4719},
        {'id': 2, 'e_m': 12.946058, 'e_o_k': [2.652881, 2.122305, 1.697844], 'p_i': 40, 'u_i': 1.0831},
        {'id': 3, 'e_m': 5.641397, 'e_o_k': [0.839094, 0.671275, 0.537020, 0.429616, 0.343693], 'p_i': 80, 'u_i': 3.5025},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399987, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399987, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.863900, 'e_o_k': [0.388138, 0.310510, 0.248408, 0.198727, 0.158981, 0.127185], 'p_i': 10, 'u_i': 2.2803},
        {'id': 1, 'e_m': 2.474738, 'e_o_k': [0.335396, 0.268317, 0.214653, 0.171723, 0.137378, 0.109903], 'p_i': 20, 'u_i': 3.9685},
        {'id': 2, 'e_m': 9.121090, 'e_o_k': [2.533636, 2.026909], 'p_i': 40, 'u_i': 1.4001},
        {'id': 3, 'e_m': 12.947663, 'e_o_k': [2.193032, 1.754426, 1.403541, 1.122833], 'p_i': 80, 'u_i': 2.1780},
    ]
    B_BUDGET = 110.399987
    return processors, tasks, B_BUDGET

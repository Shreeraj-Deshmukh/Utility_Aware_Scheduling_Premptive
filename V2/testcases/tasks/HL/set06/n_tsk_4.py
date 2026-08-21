"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399995, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1006, "set": 6, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.380368, 'e_o_k': [0.322606, 0.258085, 0.206468, 0.165174, 0.132139, 0.105712], 'p_i': 10, 'u_i': 2.2901},
        {'id': 1, 'e_m': 5.865049, 'e_o_k': [1.629180, 1.303344], 'p_i': 20, 'u_i': 4.0645},
        {'id': 2, 'e_m': 10.615229, 'e_o_k': [1.438659, 1.150927, 0.920742, 0.736593, 0.589275, 0.471420], 'p_i': 40, 'u_i': 4.5754},
        {'id': 3, 'e_m': 0.266399, 'e_o_k': [0.045122, 0.036097, 0.028878, 0.023102], 'p_i': 80, 'u_i': 3.5388},
    ]
    B_BUDGET = 110.399995
    return processors, tasks, B_BUDGET

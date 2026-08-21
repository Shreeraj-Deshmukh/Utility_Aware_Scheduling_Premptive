"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.135304, 'e_o_k': [0.437562, 0.350050, 0.280040], 'p_i': 10, 'u_i': 4.1455},
        {'id': 1, 'e_m': 1.429944, 'e_o_k': [0.242199, 0.193759, 0.155008, 0.124006], 'p_i': 20, 'u_i': 1.8811},
        {'id': 2, 'e_m': 5.992960, 'e_o_k': [1.228066, 0.982452, 0.785962], 'p_i': 40, 'u_i': 4.6061},
        {'id': 3, 'e_m': 29.211870, 'e_o_k': [4.344936, 3.475948, 2.780759, 2.224607, 1.779686], 'p_i': 80, 'u_i': 1.8658},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET

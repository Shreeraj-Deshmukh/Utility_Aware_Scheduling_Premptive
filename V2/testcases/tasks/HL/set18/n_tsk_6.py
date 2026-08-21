"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1018, "set": 18, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.359767, 'e_o_k': [0.278641, 0.222913, 0.178330], 'p_i': 10, 'u_i': 4.6061},
        {'id': 1, 'e_m': 0.835820, 'e_o_k': [0.124319, 0.099455, 0.079564, 0.063651, 0.050921], 'p_i': 20, 'u_i': 1.8658},
        {'id': 2, 'e_m': 2.695014, 'e_o_k': [0.748615, 0.598892], 'p_i': 40, 'u_i': 4.6317},
        {'id': 3, 'e_m': 7.874175, 'e_o_k': [1.171194, 0.936956, 0.749564, 0.599652, 0.479721], 'p_i': 80, 'u_i': 4.1058},
        {'id': 4, 'e_m': 3.900102, 'e_o_k': [0.799201, 0.639361, 0.511489], 'p_i': 40, 'u_i': 1.5782},
        {'id': 5, 'e_m': 7.178543, 'e_o_k': [1.067727, 0.854182, 0.683345, 0.546676, 0.437341], 'p_i': 20, 'u_i': 1.2072},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET

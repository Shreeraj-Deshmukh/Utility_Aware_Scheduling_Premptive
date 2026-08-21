"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1046, "set": 46, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.287998, 'e_o_k': [0.635555, 0.508444], 'p_i': 10, 'u_i': 4.4595},
        {'id': 1, 'e_m': 6.470295, 'e_o_k': [1.325880, 1.060704, 0.848563], 'p_i': 20, 'u_i': 4.0510},
        {'id': 2, 'e_m': 1.303191, 'e_o_k': [0.220730, 0.176584, 0.141267, 0.113014], 'p_i': 40, 'u_i': 2.0180},
        {'id': 3, 'e_m': 17.208455, 'e_o_k': [2.559563, 2.047651, 1.638120, 1.310496, 1.048397], 'p_i': 80, 'u_i': 3.1313},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET

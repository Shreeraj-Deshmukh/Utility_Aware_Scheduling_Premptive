"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.39998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1076, "set": 76, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.325171, 'e_o_k': [0.315125, 0.252100, 0.201680, 0.161344, 0.129075, 0.103260], 'p_i': 10, 'u_i': 2.0153},
        {'id': 1, 'e_m': 9.308795, 'e_o_k': [1.384578, 1.107662, 0.886130, 0.708904, 0.567123], 'p_i': 20, 'u_i': 4.1190},
        {'id': 2, 'e_m': 1.500088, 'e_o_k': [0.307395, 0.245916, 0.196733], 'p_i': 40, 'u_i': 4.7975},
        {'id': 3, 'e_m': 5.163273, 'e_o_k': [0.699767, 0.559814, 0.447851, 0.358281, 0.286625, 0.229300], 'p_i': 80, 'u_i': 4.0424},
    ]
    B_BUDGET = 110.399980
    return processors, tasks, B_BUDGET

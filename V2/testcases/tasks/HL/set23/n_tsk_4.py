"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399998, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.699186, 'e_o_k': [0.252735, 0.202188, 0.161750, 0.129400, 0.103520], 'p_i': 10, 'u_i': 2.2469},
        {'id': 1, 'e_m': 4.131054, 'e_o_k': [0.614448, 0.491558, 0.393246, 0.314597, 0.251678], 'p_i': 20, 'u_i': 2.3819},
        {'id': 2, 'e_m': 0.073268, 'e_o_k': [0.012410, 0.009928, 0.007942, 0.006354], 'p_i': 40, 'u_i': 2.4700},
        {'id': 3, 'e_m': 33.735759, 'e_o_k': [5.017813, 4.014250, 3.211400, 2.569120, 2.055296], 'p_i': 80, 'u_i': 2.1021},
    ]
    B_BUDGET = 110.399998
    return processors, tasks, B_BUDGET

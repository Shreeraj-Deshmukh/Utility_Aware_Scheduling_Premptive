"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399984, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399984, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.699031, 'e_o_k': [0.103973, 0.083178, 0.066543, 0.053234, 0.042587], 'p_i': 10, 'u_i': 3.1382},
        {'id': 1, 'e_m': 0.284346, 'e_o_k': [0.042293, 0.033835, 0.027068, 0.021654, 0.017323], 'p_i': 20, 'u_i': 3.0103},
        {'id': 2, 'e_m': 14.461026, 'e_o_k': [2.963325, 2.370660, 1.896528], 'p_i': 40, 'u_i': 3.7408},
        {'id': 3, 'e_m': 8.776006, 'e_o_k': [2.437779, 1.950223], 'p_i': 80, 'u_i': 2.8589},
        {'id': 4, 'e_m': 8.970280, 'e_o_k': [1.838172, 1.470538, 1.176430], 'p_i': 40, 'u_i': 2.7598},
        {'id': 5, 'e_m': 0.203968, 'e_o_k': [0.056658, 0.045326], 'p_i': 10, 'u_i': 2.0735},
    ]
    B_BUDGET = 110.399984
    return processors, tasks, B_BUDGET

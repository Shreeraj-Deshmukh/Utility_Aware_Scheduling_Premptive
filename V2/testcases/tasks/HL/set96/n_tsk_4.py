"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.399993, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1096, "set": 96, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.750674, 'e_o_k': [0.260393, 0.208314, 0.166651, 0.133321, 0.106657], 'p_i': 10, 'u_i': 3.1382},
        {'id': 1, 'e_m': 8.889805, 'e_o_k': [1.322258, 1.057806, 0.846245, 0.676996, 0.541597], 'p_i': 20, 'u_i': 3.0103},
        {'id': 2, 'e_m': 5.268379, 'e_o_k': [1.079586, 0.863669, 0.690935], 'p_i': 40, 'u_i': 3.7408},
        {'id': 3, 'e_m': 3.898632, 'e_o_k': [1.082953, 0.866363], 'p_i': 80, 'u_i': 2.8589},
    ]
    B_BUDGET = 110.399993
    return processors, tasks, B_BUDGET

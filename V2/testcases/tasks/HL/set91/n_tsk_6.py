"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399988, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399988, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1091, "set": 91, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.480132, 'e_o_k': [0.200599, 0.160479, 0.128383, 0.102707, 0.082165, 0.065732], 'p_i': 10, 'u_i': 3.3094},
        {'id': 1, 'e_m': 0.550568, 'e_o_k': [0.112821, 0.090257, 0.072206], 'p_i': 20, 'u_i': 3.8452},
        {'id': 2, 'e_m': 16.779335, 'e_o_k': [2.274066, 1.819253, 1.455403, 1.164322, 0.931458, 0.745166], 'p_i': 40, 'u_i': 1.8919},
        {'id': 3, 'e_m': 7.849433, 'e_o_k': [1.063816, 0.851053, 0.680842, 0.544674, 0.435739, 0.348591], 'p_i': 80, 'u_i': 3.0558},
        {'id': 4, 'e_m': 0.184203, 'e_o_k': [0.031200, 0.024960, 0.019968, 0.015974], 'p_i': 10, 'u_i': 1.4898},
        {'id': 5, 'e_m': 3.537470, 'e_o_k': [0.599165, 0.479332, 0.383466, 0.306773], 'p_i': 40, 'u_i': 1.5566},
    ]
    B_BUDGET = 110.399988
    return processors, tasks, B_BUDGET

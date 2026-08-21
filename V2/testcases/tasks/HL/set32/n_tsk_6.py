"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399997, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399997, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1032, "set": 32, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.384353, 'e_o_k': [0.234477, 0.187582, 0.150065, 0.120052], 'p_i': 10, 'u_i': 1.0669},
        {'id': 1, 'e_m': 1.854864, 'e_o_k': [0.314171, 0.251337, 0.201069, 0.160855], 'p_i': 20, 'u_i': 2.5210},
        {'id': 2, 'e_m': 1.794964, 'e_o_k': [0.367820, 0.294256, 0.235405], 'p_i': 40, 'u_i': 3.1907},
        {'id': 3, 'e_m': 17.552391, 'e_o_k': [2.972966, 2.378373, 1.902698, 1.522159], 'p_i': 80, 'u_i': 4.8710},
        {'id': 4, 'e_m': 3.295999, 'e_o_k': [0.915555, 0.732444], 'p_i': 20, 'u_i': 3.8865},
        {'id': 5, 'e_m': 1.397426, 'e_o_k': [0.388174, 0.310539], 'p_i': 10, 'u_i': 3.2848},
    ]
    B_BUDGET = 110.399997
    return processors, tasks, B_BUDGET

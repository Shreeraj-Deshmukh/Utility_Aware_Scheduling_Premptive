"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399983, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 110.399983, "H": 80, "J": 29, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1048, "set": 48, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.372012, 'e_o_k': [0.381114, 0.304891], 'p_i': 10, 'u_i': 2.9117},
        {'id': 1, 'e_m': 3.488332, 'e_o_k': [0.714822, 0.571858, 0.457486], 'p_i': 20, 'u_i': 3.4870},
        {'id': 2, 'e_m': 0.095964, 'e_o_k': [0.019665, 0.015732, 0.012585], 'p_i': 40, 'u_i': 2.7836},
        {'id': 3, 'e_m': 3.859529, 'e_o_k': [1.072091, 0.857673], 'p_i': 80, 'u_i': 2.5957},
        {'id': 4, 'e_m': 11.637726, 'e_o_k': [3.232702, 2.586161], 'p_i': 80, 'u_i': 3.2394},
        {'id': 5, 'e_m': 2.185253, 'e_o_k': [0.325032, 0.260025, 0.208020, 0.166416, 0.133133], 'p_i': 20, 'u_i': 3.4917},
        {'id': 6, 'e_m': 1.684152, 'e_o_k': [0.250499, 0.200399, 0.160319, 0.128255, 0.102604], 'p_i': 10, 'u_i': 3.3989},
        {'id': 7, 'e_m': 1.167163, 'e_o_k': [0.173602, 0.138882, 0.111105, 0.088884, 0.071107], 'p_i': 80, 'u_i': 2.7388},
    ]
    B_BUDGET = 110.399983
    return processors, tasks, B_BUDGET

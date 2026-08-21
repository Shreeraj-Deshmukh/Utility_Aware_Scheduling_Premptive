"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399994, "H": 80, "J": 23, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "freq", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399994, "H": 80, "J": 23, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1095, "set": 95, "sweep": "freq", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.583822, 'e_o_k': [0.268262, 0.214610, 0.171688, 0.137350], 'p_i': 10, 'u_i': 1.9313},
        {'id': 1, 'e_m': 2.910187, 'e_o_k': [0.808385, 0.646708], 'p_i': 20, 'u_i': 4.0147},
        {'id': 2, 'e_m': 6.823232, 'e_o_k': [0.924738, 0.739790, 0.591832, 0.473466, 0.378773, 0.303018], 'p_i': 40, 'u_i': 3.8759},
        {'id': 3, 'e_m': 3.019671, 'e_o_k': [0.618785, 0.495028, 0.396022], 'p_i': 80, 'u_i': 4.3076},
        {'id': 4, 'e_m': 3.916411, 'e_o_k': [0.530783, 0.424626, 0.339701, 0.271761, 0.217409, 0.173927], 'p_i': 80, 'u_i': 1.9116},
        {'id': 5, 'e_m': 2.706466, 'e_o_k': [0.554604, 0.443683, 0.354946], 'p_i': 40, 'u_i': 2.7475},
        {'id': 6, 'e_m': 8.231295, 'e_o_k': [1.224312, 0.979450, 0.783560, 0.626848, 0.501478], 'p_i': 80, 'u_i': 2.9584},
        {'id': 7, 'e_m': 1.365476, 'e_o_k': [0.231280, 0.185024, 0.148019, 0.118415], 'p_i': 20, 'u_i': 3.8181},
    ]
    B_BUDGET = 110.399994
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399999, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 110.399999, "H": 80, "J": 24, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.443349, 'e_o_k': [0.313009, 0.187806, 0.112683, 0.067610, 0.040566], 'p_i': 10, 'u_i': 4.7302},
        {'id': 1, 'e_m': 4.992277, 'e_o_k': [1.560087, 0.936052], 'p_i': 20, 'u_i': 1.8342},
        {'id': 2, 'e_m': 1.773001, 'e_o_k': [0.452296, 0.271378, 0.162827], 'p_i': 40, 'u_i': 2.1428},
        {'id': 3, 'e_m': 4.820922, 'e_o_k': [1.107749, 0.664649, 0.398790, 0.239274], 'p_i': 80, 'u_i': 3.7337},
        {'id': 4, 'e_m': 5.896724, 'e_o_k': [1.278783, 0.767270, 0.460362, 0.276217, 0.165730], 'p_i': 40, 'u_i': 3.4112},
        {'id': 5, 'e_m': 9.193774, 'e_o_k': [2.873054, 1.723833], 'p_i': 80, 'u_i': 2.7179},
        {'id': 6, 'e_m': 0.009519, 'e_o_k': [0.002187, 0.001312, 0.000787, 0.000472], 'p_i': 40, 'u_i': 2.6898},
        {'id': 7, 'e_m': 0.777730, 'e_o_k': [0.198400, 0.119040, 0.071424], 'p_i': 20, 'u_i': 4.5690},
    ]
    B_BUDGET = 110.399999
    return processors, tasks, B_BUDGET

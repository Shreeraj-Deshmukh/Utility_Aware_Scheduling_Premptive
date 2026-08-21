"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399992, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 110.399992, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1085, "set": 85, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.488440, 'e_o_k': [0.100090, 0.080072, 0.064058], 'p_i': 10, 'u_i': 1.2408},
        {'id': 1, 'e_m': 0.924655, 'e_o_k': [0.189479, 0.151583, 0.121266], 'p_i': 20, 'u_i': 2.7274},
        {'id': 2, 'e_m': 2.288327, 'e_o_k': [0.468919, 0.375136, 0.300108], 'p_i': 40, 'u_i': 3.7398},
        {'id': 3, 'e_m': 4.657210, 'e_o_k': [0.954346, 0.763477, 0.610782], 'p_i': 80, 'u_i': 1.4758},
        {'id': 4, 'e_m': 0.144768, 'e_o_k': [0.029665, 0.023732, 0.018986], 'p_i': 10, 'u_i': 4.3036},
        {'id': 5, 'e_m': 0.140954, 'e_o_k': [0.028884, 0.023107, 0.018486], 'p_i': 40, 'u_i': 3.9596},
        {'id': 6, 'e_m': 4.924673, 'e_o_k': [1.009154, 0.807323, 0.645859], 'p_i': 20, 'u_i': 3.9830},
        {'id': 7, 'e_m': 3.252657, 'e_o_k': [0.666528, 0.533222, 0.426578], 'p_i': 10, 'u_i': 3.3191},
    ]
    B_BUDGET = 110.399992
    return processors, tasks, B_BUDGET

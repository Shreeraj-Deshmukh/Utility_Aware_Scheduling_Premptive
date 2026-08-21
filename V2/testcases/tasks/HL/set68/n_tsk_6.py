"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.399983, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.399983, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1068, "set": 68, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.271833, 'e_o_k': [0.215419, 0.172335, 0.137868, 0.110294], 'p_i': 10, 'u_i': 4.9351},
        {'id': 1, 'e_m': 4.379754, 'e_o_k': [0.651439, 0.521151, 0.416921, 0.333537, 0.266829], 'p_i': 20, 'u_i': 4.9277},
        {'id': 2, 'e_m': 3.696436, 'e_o_k': [0.626090, 0.500872, 0.400698, 0.320558], 'p_i': 40, 'u_i': 1.3099},
        {'id': 3, 'e_m': 11.223342, 'e_o_k': [1.900973, 1.520778, 1.216622, 0.973298], 'p_i': 80, 'u_i': 1.1502},
        {'id': 4, 'e_m': 0.604848, 'e_o_k': [0.123944, 0.099155, 0.079324], 'p_i': 10, 'u_i': 2.1747},
        {'id': 5, 'e_m': 3.212830, 'e_o_k': [0.892453, 0.713962], 'p_i': 20, 'u_i': 4.4262},
    ]
    B_BUDGET = 110.399983
    return processors, tasks, B_BUDGET

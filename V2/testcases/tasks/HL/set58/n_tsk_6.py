"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.39999, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.39999, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.705361, 'e_o_k': [0.473711, 0.378969], 'p_i': 10, 'u_i': 1.4573},
        {'id': 1, 'e_m': 5.058743, 'e_o_k': [0.752431, 0.601945, 0.481556, 0.385245, 0.308196], 'p_i': 20, 'u_i': 1.2598},
        {'id': 2, 'e_m': 0.721156, 'e_o_k': [0.097737, 0.078189, 0.062551, 0.050041, 0.040033, 0.032026], 'p_i': 40, 'u_i': 4.1820},
        {'id': 3, 'e_m': 7.352609, 'e_o_k': [2.042391, 1.633913], 'p_i': 80, 'u_i': 2.8729},
        {'id': 4, 'e_m': 2.676730, 'e_o_k': [0.548510, 0.438808, 0.351047], 'p_i': 20, 'u_i': 4.4646},
        {'id': 5, 'e_m': 1.327537, 'e_o_k': [0.368760, 0.295008], 'p_i': 10, 'u_i': 2.8456},
    ]
    B_BUDGET = 110.399990
    return processors, tasks, B_BUDGET

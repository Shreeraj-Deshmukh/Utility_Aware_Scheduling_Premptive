"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520001, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.029816, 'e_o_k': [0.126617, 0.101293, 0.081035], 'p_i': 10, 'u_i': 3.5588},
        {'id': 1, 'e_m': 2.374109, 'e_o_k': [0.395685, 0.316548], 'p_i': 20, 'u_i': 1.0875},
        {'id': 2, 'e_m': 7.660706, 'e_o_k': [0.778527, 0.622822, 0.498257, 0.398606], 'p_i': 40, 'u_i': 2.9446},
        {'id': 3, 'e_m': 0.338684, 'e_o_k': [0.034419, 0.027535, 0.022028, 0.017623], 'p_i': 80, 'u_i': 2.5289},
        {'id': 4, 'e_m': 15.042607, 'e_o_k': [1.342451, 1.073960, 0.859168, 0.687335, 0.549868], 'p_i': 40, 'u_i': 2.8941},
        {'id': 5, 'e_m': 8.086256, 'e_o_k': [0.657547, 0.526038, 0.420830, 0.336664, 0.269331, 0.215465], 'p_i': 40, 'u_i': 4.5618},
        {'id': 6, 'e_m': 0.399581, 'e_o_k': [0.066597, 0.053277], 'p_i': 10, 'u_i': 3.9189},
        {'id': 7, 'e_m': 6.575284, 'e_o_k': [0.668220, 0.534576, 0.427661, 0.342129], 'p_i': 40, 'u_i': 2.1344},
    ]
    B_BUDGET = 143.520001
    return processors, tasks, B_BUDGET

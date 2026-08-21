"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 55.200009, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1015, "set": 15, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.120379, 'e_o_k': [0.315382, 0.252306, 0.201845, 0.161476, 0.129181], 'p_i': 10, 'u_i': 3.0940},
        {'id': 1, 'e_m': 1.696977, 'e_o_k': [0.252406, 0.201925, 0.161540, 0.129232, 0.103386], 'p_i': 20, 'u_i': 2.1175},
        {'id': 2, 'e_m': 0.270623, 'e_o_k': [0.036677, 0.029342, 0.023473, 0.018779, 0.015023, 0.012018], 'p_i': 40, 'u_i': 3.6512},
        {'id': 3, 'e_m': 7.707815, 'e_o_k': [1.305524, 1.044419, 0.835536, 0.668428], 'p_i': 80, 'u_i': 2.9125},
    ]
    B_BUDGET = 55.200009
    return processors, tasks, B_BUDGET

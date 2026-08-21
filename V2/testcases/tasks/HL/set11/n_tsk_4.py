"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 110.400001, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1011, "set": 11, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.272733, 'e_o_k': [0.338043, 0.270435, 0.216348, 0.173078, 0.138463], 'p_i': 10, 'u_i': 2.5944},
        {'id': 1, 'e_m': 9.445309, 'e_o_k': [1.404883, 1.123906, 0.899125, 0.719300, 0.575440], 'p_i': 20, 'u_i': 4.8069},
        {'id': 2, 'e_m': 3.305264, 'e_o_k': [0.559835, 0.447868, 0.358294, 0.286635], 'p_i': 40, 'u_i': 1.7136},
        {'id': 3, 'e_m': 1.426372, 'e_o_k': [0.212157, 0.169725, 0.135780, 0.108624, 0.086899], 'p_i': 80, 'u_i': 3.6562},
    ]
    B_BUDGET = 110.400001
    return processors, tasks, B_BUDGET

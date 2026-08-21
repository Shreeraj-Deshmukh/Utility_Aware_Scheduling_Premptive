"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400005, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.400005, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.838384, 'e_o_k': [0.788440, 0.630752], 'p_i': 10, 'u_i': 1.9248},
        {'id': 1, 'e_m': 0.545379, 'e_o_k': [0.073914, 0.059131, 0.047305, 0.037844, 0.030275, 0.024220], 'p_i': 20, 'u_i': 3.6832},
        {'id': 2, 'e_m': 1.439061, 'e_o_k': [0.243743, 0.194995, 0.155996, 0.124797], 'p_i': 40, 'u_i': 2.0214},
        {'id': 3, 'e_m': 29.083887, 'e_o_k': [3.941675, 3.153340, 2.522672, 2.018138, 1.614510, 1.291608], 'p_i': 80, 'u_i': 3.5232},
        {'id': 4, 'e_m': 0.307476, 'e_o_k': [0.085410, 0.068328], 'p_i': 10, 'u_i': 1.0606},
        {'id': 5, 'e_m': 4.689598, 'e_o_k': [0.794309, 0.635447, 0.508358, 0.406686], 'p_i': 80, 'u_i': 3.4010},
    ]
    B_BUDGET = 110.400005
    return processors, tasks, B_BUDGET

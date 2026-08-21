"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1042, "set": 42, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.969754, 'e_o_k': [0.403872, 0.323098, 0.258478, 0.206782, 0.165426], 'p_i': 10, 'u_i': 2.8937},
        {'id': 1, 'e_m': 1.381909, 'e_o_k': [0.655377, 0.524301, 0.419441, 0.335553], 'p_i': 20, 'u_i': 3.5048},
        {'id': 2, 'e_m': 0.206917, 'e_o_k': [0.078520, 0.062816, 0.050253, 0.040202, 0.032162, 0.025730], 'p_i': 40, 'u_i': 4.5166},
        {'id': 3, 'e_m': 1.087762, 'e_o_k': [0.515876, 0.412701, 0.330161, 0.264129], 'p_i': 80, 'u_i': 1.0922},
        {'id': 4, 'e_m': 4.395290, 'e_o_k': [3.418559, 2.734847], 'p_i': 40, 'u_i': 2.4300},
        {'id': 5, 'e_m': 2.105539, 'e_o_k': [0.876890, 0.701512, 0.561210, 0.448968, 0.359174], 'p_i': 20, 'u_i': 4.3958},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET

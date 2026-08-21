"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 110.40001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067754, 'e_o_k': [0.180853, 0.144682, 0.115746, 0.092597], 'p_i': 10, 'u_i': 2.4700},
        {'id': 1, 'e_m': 2.497461, 'e_o_k': [0.371469, 0.297175, 0.237740, 0.190192, 0.152154], 'p_i': 20, 'u_i': 2.1021},
        {'id': 2, 'e_m': 0.032821, 'e_o_k': [0.004448, 0.003559, 0.002847, 0.002277, 0.001822, 0.001458], 'p_i': 40, 'u_i': 2.0660},
        {'id': 3, 'e_m': 15.907726, 'e_o_k': [4.418813, 3.535050], 'p_i': 80, 'u_i': 3.5059},
        {'id': 4, 'e_m': 29.428276, 'e_o_k': [6.030384, 4.824308, 3.859446], 'p_i': 80, 'u_i': 1.7742},
        {'id': 5, 'e_m': 0.033241, 'e_o_k': [0.006812, 0.005449, 0.004359], 'p_i': 40, 'u_i': 1.4108},
    ]
    B_BUDGET = 110.400010
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.4, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.511173, 'e_o_k': [0.867067, 0.693653, 0.554923], 'p_i': 10, 'u_i': 2.2612},
        {'id': 1, 'e_m': 3.773415, 'e_o_k': [1.789560, 1.431648, 1.145318, 0.916255], 'p_i': 20, 'u_i': 2.3936},
        {'id': 2, 'e_m': 12.214956, 'e_o_k': [5.793001, 4.634401, 3.707520, 2.966016], 'p_i': 40, 'u_i': 4.7316},
        {'id': 3, 'e_m': 12.387043, 'e_o_k': [5.874614, 4.699691, 3.759753, 3.007802], 'p_i': 80, 'u_i': 1.7602},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET

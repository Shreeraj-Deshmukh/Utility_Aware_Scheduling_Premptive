"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319994, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1088, "set": 88, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.755587, 'e_o_k': [0.433533, 0.346827, 0.277461], 'p_i': 10, 'u_i': 2.2612},
        {'id': 1, 'e_m': 1.886707, 'e_o_k': [0.894780, 0.715824, 0.572659, 0.458127], 'p_i': 20, 'u_i': 2.3936},
        {'id': 2, 'e_m': 6.107478, 'e_o_k': [2.896500, 2.317200, 1.853760, 1.483008], 'p_i': 40, 'u_i': 4.7316},
        {'id': 3, 'e_m': 6.193521, 'e_o_k': [2.937307, 2.349846, 1.879876, 1.503901], 'p_i': 80, 'u_i': 1.7602},
    ]
    B_BUDGET = 88.319994
    return processors, tasks, B_BUDGET

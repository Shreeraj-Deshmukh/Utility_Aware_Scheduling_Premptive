"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319991, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1050, "set": 50, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.811137, 'e_o_k': [0.337813, 0.270250, 0.216200, 0.172960, 0.138368], 'p_i': 10, 'u_i': 4.0918},
        {'id': 1, 'e_m': 0.740340, 'e_o_k': [0.308328, 0.246663, 0.197330, 0.157864, 0.126291], 'p_i': 20, 'u_i': 2.7075},
        {'id': 2, 'e_m': 2.639818, 'e_o_k': [1.251946, 1.001557, 0.801246, 0.640997], 'p_i': 40, 'u_i': 3.4005},
        {'id': 3, 'e_m': 7.095740, 'e_o_k': [5.518909, 4.415127], 'p_i': 80, 'u_i': 3.5378},
        {'id': 4, 'e_m': 0.220210, 'e_o_k': [0.083565, 0.066852, 0.053482, 0.042785, 0.034228, 0.027383], 'p_i': 10, 'u_i': 2.8954},
        {'id': 5, 'e_m': 2.103121, 'e_o_k': [0.875883, 0.700707, 0.560565, 0.448452, 0.358762], 'p_i': 20, 'u_i': 2.6615},
    ]
    B_BUDGET = 88.319991
    return processors, tasks, B_BUDGET

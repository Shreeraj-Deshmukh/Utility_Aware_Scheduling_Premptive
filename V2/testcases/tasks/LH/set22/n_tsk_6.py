"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.31999, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.31999, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1022, "set": 22, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.330362, 'e_o_k': [0.763323, 0.610658, 0.488526], 'p_i': 10, 'u_i': 2.7301},
        {'id': 1, 'e_m': 0.095834, 'e_o_k': [0.045450, 0.036360, 0.029088, 0.023270], 'p_i': 20, 'u_i': 2.9329},
        {'id': 2, 'e_m': 3.019103, 'e_o_k': [1.431824, 1.145459, 0.916367, 0.733094], 'p_i': 40, 'u_i': 4.3550},
        {'id': 3, 'e_m': 1.448272, 'e_o_k': [0.603159, 0.482528, 0.386022, 0.308818, 0.247054], 'p_i': 80, 'u_i': 2.2741},
        {'id': 4, 'e_m': 0.768295, 'e_o_k': [0.440825, 0.352660, 0.282128], 'p_i': 10, 'u_i': 2.5808},
        {'id': 5, 'e_m': 3.670463, 'e_o_k': [1.528632, 1.222905, 0.978324, 0.782659, 0.626127], 'p_i': 40, 'u_i': 4.5356},
    ]
    B_BUDGET = 88.319990
    return processors, tasks, B_BUDGET

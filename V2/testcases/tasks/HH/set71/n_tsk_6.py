"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639998, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639998, "H": 80, "J": 24, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1071, "set": 71, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 2.838384, 'e_o_k': [2.207632, 1.766105], 'p_i': 10, 'u_i': 1.9248},
        {'id': 1, 'e_m': 0.545379, 'e_o_k': [0.206959, 0.165567, 0.132454, 0.105963, 0.084771, 0.067816], 'p_i': 20, 'u_i': 3.6832},
        {'id': 2, 'e_m': 1.439061, 'e_o_k': [0.682482, 0.545985, 0.436788, 0.349431], 'p_i': 40, 'u_i': 2.0214},
        {'id': 3, 'e_m': 29.083887, 'e_o_k': [11.036691, 8.829352, 7.063482, 5.650786, 4.520628, 3.616503], 'p_i': 80, 'u_i': 3.5232},
        {'id': 4, 'e_m': 0.307476, 'e_o_k': [0.239148, 0.191318], 'p_i': 10, 'u_i': 1.0606},
        {'id': 5, 'e_m': 4.689598, 'e_o_k': [2.224064, 1.779251, 1.423401, 1.138721], 'p_i': 80, 'u_i': 3.4010},
    ]
    B_BUDGET = 176.639998
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319988, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319988, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1001, "set": 1, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.177798, 'e_o_k': [0.074047, 0.059238, 0.047390, 0.037912, 0.030330], 'p_i': 10, 'u_i': 3.8879},
        {'id': 1, 'e_m': 3.882856, 'e_o_k': [1.473458, 1.178766, 0.943013, 0.754410, 0.603528, 0.482823], 'p_i': 20, 'u_i': 3.5961},
        {'id': 2, 'e_m': 0.656943, 'e_o_k': [0.273596, 0.218877, 0.175101, 0.140081, 0.112065], 'p_i': 40, 'u_i': 4.1247},
        {'id': 3, 'e_m': 0.977487, 'e_o_k': [0.560853, 0.448682, 0.358946], 'p_i': 80, 'u_i': 3.4312},
        {'id': 4, 'e_m': 11.590635, 'e_o_k': [9.014938, 7.211951], 'p_i': 80, 'u_i': 1.1226},
        {'id': 5, 'e_m': 0.291046, 'e_o_k': [0.121211, 0.096969, 0.077575, 0.062060, 0.049648], 'p_i': 20, 'u_i': 3.8598},
    ]
    B_BUDGET = 88.319988
    return processors, tasks, B_BUDGET

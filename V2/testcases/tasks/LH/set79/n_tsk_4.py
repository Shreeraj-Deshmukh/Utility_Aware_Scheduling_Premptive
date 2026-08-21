"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}
"""

_SPEC = '{"B": 88.319997, "H": 80, "J": 15, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 4, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1079, "set": 79, "sweep": "tasks", "util_per_core": 0.2, "value": "4"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.748978, 'e_o_k': [0.429741, 0.343793, 0.275035], 'p_i': 10, 'u_i': 4.6460},
        {'id': 1, 'e_m': 2.001687, 'e_o_k': [0.759596, 0.607677, 0.486141, 0.388913, 0.311131, 0.248904], 'p_i': 20, 'u_i': 1.6535},
        {'id': 2, 'e_m': 0.867381, 'e_o_k': [0.361237, 0.288990, 0.231192, 0.184953, 0.147963], 'p_i': 40, 'u_i': 3.3613},
        {'id': 3, 'e_m': 16.266664, 'e_o_k': [7.714542, 6.171634, 4.937307, 3.949846], 'p_i': 80, 'u_i': 3.4647},
    ]
    B_BUDGET = 88.319997
    return processors, tasks, B_BUDGET

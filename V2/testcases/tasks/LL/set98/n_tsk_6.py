"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.200002, "H": 80, "J": 20, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1098, "set": 98, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.172281, 'e_o_k': [0.325634, 0.260507], 'p_i': 10, 'u_i': 3.5492},
        {'id': 1, 'e_m': 0.828834, 'e_o_k': [0.230232, 0.184185], 'p_i': 20, 'u_i': 2.1494},
        {'id': 2, 'e_m': 3.164984, 'e_o_k': [0.428943, 0.343155, 0.274524, 0.219619, 0.175695, 0.140556], 'p_i': 40, 'u_i': 1.9189},
        {'id': 3, 'e_m': 0.143966, 'e_o_k': [0.039990, 0.031992], 'p_i': 80, 'u_i': 2.3334},
        {'id': 4, 'e_m': 0.630351, 'e_o_k': [0.129170, 0.103336, 0.082669], 'p_i': 80, 'u_i': 2.9112},
        {'id': 5, 'e_m': 3.050532, 'e_o_k': [0.453732, 0.362986, 0.290389, 0.232311, 0.185849], 'p_i': 20, 'u_i': 2.1467},
    ]
    B_BUDGET = 55.200002
    return processors, tasks, B_BUDGET

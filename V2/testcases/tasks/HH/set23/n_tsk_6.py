"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640001, "H": 80, "J": 18, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1023, "set": 23, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.067754, 'e_o_k': [0.506387, 0.405110, 0.324088, 0.259270], 'p_i': 10, 'u_i': 2.4700},
        {'id': 1, 'e_m': 2.497461, 'e_o_k': [1.040113, 0.832091, 0.665673, 0.532538, 0.426030], 'p_i': 20, 'u_i': 2.1021},
        {'id': 2, 'e_m': 0.032821, 'e_o_k': [0.012455, 0.009964, 0.007971, 0.006377, 0.005102, 0.004081], 'p_i': 40, 'u_i': 2.0660},
        {'id': 3, 'e_m': 15.907726, 'e_o_k': [12.372676, 9.898141], 'p_i': 80, 'u_i': 3.5059},
        {'id': 4, 'e_m': 29.428276, 'e_o_k': [16.885076, 13.508061, 10.806449], 'p_i': 80, 'u_i': 1.7742},
        {'id': 5, 'e_m': 0.033241, 'e_o_k': [0.019073, 0.015258, 0.012207], 'p_i': 40, 'u_i': 1.4108},
    ]
    B_BUDGET = 176.640001
    return processors, tasks, B_BUDGET

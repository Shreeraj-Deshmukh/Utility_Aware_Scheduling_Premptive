"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320003, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320003, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1016, "set": 16, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.730518, 'e_o_k': [0.304238, 0.243390, 0.194712, 0.155770, 0.124616], 'p_i': 10, 'u_i': 1.1399},
        {'id': 1, 'e_m': 1.370039, 'e_o_k': [0.519900, 0.415920, 0.332736, 0.266189, 0.212951, 0.170361], 'p_i': 20, 'u_i': 4.6324},
        {'id': 2, 'e_m': 3.061509, 'e_o_k': [1.275021, 1.020017, 0.816014, 0.652811, 0.522249], 'p_i': 40, 'u_i': 3.3557},
        {'id': 3, 'e_m': 3.659807, 'e_o_k': [1.524194, 1.219355, 0.975484, 0.780387, 0.624310], 'p_i': 80, 'u_i': 3.4396},
        {'id': 4, 'e_m': 0.485795, 'e_o_k': [0.184348, 0.147479, 0.117983, 0.094386, 0.075509, 0.060407], 'p_i': 10, 'u_i': 2.9972},
        {'id': 5, 'e_m': 3.503257, 'e_o_k': [2.724755, 2.179804], 'p_i': 40, 'u_i': 3.3467},
    ]
    B_BUDGET = 88.320003
    return processors, tasks, B_BUDGET

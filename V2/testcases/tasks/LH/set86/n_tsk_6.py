"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319985, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319985, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.070133, 'e_o_k': [0.026614, 0.021291, 0.017033, 0.013626, 0.010901, 0.008721], 'p_i': 10, 'u_i': 3.8731},
        {'id': 1, 'e_m': 0.306792, 'e_o_k': [0.176028, 0.140823, 0.112658], 'p_i': 20, 'u_i': 4.5676},
        {'id': 2, 'e_m': 1.897257, 'e_o_k': [0.899783, 0.719826, 0.575861, 0.460689], 'p_i': 40, 'u_i': 2.8991},
        {'id': 3, 'e_m': 11.381869, 'e_o_k': [4.740188, 3.792151, 3.033720, 2.426976, 1.941581], 'p_i': 80, 'u_i': 1.9490},
        {'id': 4, 'e_m': 1.044862, 'e_o_k': [0.812670, 0.650136], 'p_i': 20, 'u_i': 1.1516},
        {'id': 5, 'e_m': 5.427967, 'e_o_k': [3.114407, 2.491526, 1.993221], 'p_i': 40, 'u_i': 2.6742},
    ]
    B_BUDGET = 88.319985
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639999, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639999, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1026, "set": 26, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.157033, 'e_o_k': [1.577502, 1.262002, 1.009601, 0.807681, 0.646145, 0.516916], 'p_i': 10, 'u_i': 2.2803},
        {'id': 1, 'e_m': 1.308705, 'e_o_k': [0.496625, 0.397300, 0.317840, 0.254272, 0.203417, 0.162734], 'p_i': 20, 'u_i': 3.9685},
        {'id': 2, 'e_m': 3.452694, 'e_o_k': [2.685428, 2.148343], 'p_i': 40, 'u_i': 1.4001},
        {'id': 3, 'e_m': 9.033558, 'e_o_k': [4.284208, 3.427366, 2.741893, 2.193514], 'p_i': 80, 'u_i': 2.1780},
        {'id': 4, 'e_m': 4.055672, 'e_o_k': [2.327025, 1.861620, 1.489296], 'p_i': 80, 'u_i': 3.8388},
        {'id': 5, 'e_m': 5.514294, 'e_o_k': [2.615180, 2.092144, 1.673715, 1.338972], 'p_i': 80, 'u_i': 1.0041},
    ]
    B_BUDGET = 176.639999
    return processors, tasks, B_BUDGET

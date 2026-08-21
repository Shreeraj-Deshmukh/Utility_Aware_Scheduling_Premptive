"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199993, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199993, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.482155, 'e_o_k': [0.071715, 0.057372, 0.045898, 0.036718, 0.029375], 'p_i': 10, 'u_i': 3.2309},
        {'id': 1, 'e_m': 4.321063, 'e_o_k': [0.642709, 0.514167, 0.411334, 0.329067, 0.263254], 'p_i': 20, 'u_i': 2.9440},
        {'id': 2, 'e_m': 0.240290, 'e_o_k': [0.049240, 0.039392, 0.031513], 'p_i': 40, 'u_i': 1.5741},
        {'id': 3, 'e_m': 2.229082, 'e_o_k': [0.302103, 0.241682, 0.193346, 0.154677, 0.123741, 0.098993], 'p_i': 80, 'u_i': 1.4817},
        {'id': 4, 'e_m': 2.063041, 'e_o_k': [0.573067, 0.458454], 'p_i': 40, 'u_i': 3.4660},
        {'id': 5, 'e_m': 1.005690, 'e_o_k': [0.136299, 0.109039, 0.087231, 0.069785, 0.055828, 0.044662], 'p_i': 20, 'u_i': 3.9304},
    ]
    B_BUDGET = 55.199993
    return processors, tasks, B_BUDGET

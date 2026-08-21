"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320005, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320005, "H": 80, "J": 17, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1077, "set": 77, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.304154, 'e_o_k': [0.174515, 0.139612, 0.111689], 'p_i': 10, 'u_i': 2.5184},
        {'id': 1, 'e_m': 2.335008, 'e_o_k': [0.972457, 0.777966, 0.622373, 0.497898, 0.398318], 'p_i': 20, 'u_i': 4.2996},
        {'id': 2, 'e_m': 3.020032, 'e_o_k': [1.146035, 0.916828, 0.733462, 0.586770, 0.469416, 0.375533], 'p_i': 40, 'u_i': 3.3901},
        {'id': 3, 'e_m': 0.952703, 'e_o_k': [0.361530, 0.289224, 0.231379, 0.185103, 0.148083, 0.118466], 'p_i': 80, 'u_i': 2.3217},
        {'id': 4, 'e_m': 10.325824, 'e_o_k': [4.897071, 3.917657, 3.134125, 2.507300], 'p_i': 80, 'u_i': 2.1118},
        {'id': 5, 'e_m': 2.908145, 'e_o_k': [1.379201, 1.103361, 0.882689, 0.706151], 'p_i': 80, 'u_i': 4.2305},
    ]
    B_BUDGET = 88.320005
    return processors, tasks, B_BUDGET

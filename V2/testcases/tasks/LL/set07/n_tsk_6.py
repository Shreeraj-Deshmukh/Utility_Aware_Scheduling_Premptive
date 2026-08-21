"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199999, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 55.199999, "H": 80, "J": 23, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1007, "set": 7, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.122529, 'e_o_k': [0.016606, 0.013285, 0.010628, 0.008502, 0.006802, 0.005441], 'p_i': 10, 'u_i': 4.9047},
        {'id': 1, 'e_m': 0.419662, 'e_o_k': [0.085996, 0.068797, 0.055038], 'p_i': 20, 'u_i': 3.2321},
        {'id': 2, 'e_m': 2.339399, 'e_o_k': [0.347959, 0.278367, 0.222694, 0.178155, 0.142524], 'p_i': 40, 'u_i': 3.3144},
        {'id': 3, 'e_m': 1.435058, 'e_o_k': [0.194490, 0.155592, 0.124474, 0.099579, 0.079663, 0.063731], 'p_i': 80, 'u_i': 1.1307},
        {'id': 4, 'e_m': 1.500724, 'e_o_k': [0.223216, 0.178573, 0.142858, 0.114286, 0.091429], 'p_i': 20, 'u_i': 4.3260},
        {'id': 5, 'e_m': 4.306093, 'e_o_k': [0.882396, 0.705917, 0.564733], 'p_i': 20, 'u_i': 4.7000},
    ]
    B_BUDGET = 55.199999
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639993, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.639993, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1084, "set": 84, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.670616, 'e_o_k': [0.254484, 0.203587, 0.162870, 0.130296, 0.104237, 0.083389], 'p_i': 10, 'u_i': 3.3883},
        {'id': 1, 'e_m': 1.064349, 'e_o_k': [0.443268, 0.354614, 0.283691, 0.226953, 0.181562], 'p_i': 20, 'u_i': 2.1673},
        {'id': 2, 'e_m': 6.847533, 'e_o_k': [2.598487, 2.078790, 1.663032, 1.330425, 1.064340, 0.851472], 'p_i': 40, 'u_i': 3.4649},
        {'id': 3, 'e_m': 4.269330, 'e_o_k': [2.024750, 1.619800, 1.295840, 1.036672], 'p_i': 80, 'u_i': 2.8434},
        {'id': 4, 'e_m': 0.700141, 'e_o_k': [0.401720, 0.321376, 0.257101], 'p_i': 20, 'u_i': 4.3788},
        {'id': 5, 'e_m': 4.201589, 'e_o_k': [1.992624, 1.594099, 1.275279, 1.020223], 'p_i': 10, 'u_i': 3.2500},
    ]
    B_BUDGET = 176.639993
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640014, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}
"""

_SPEC = '{"B": 176.640014, "H": 80, "J": 25, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1064, "set": 64, "sweep": "tasks", "util_per_core": 0.4, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.944933, 'e_o_k': [0.922394, 0.737915, 0.590332, 0.472266], 'p_i': 10, 'u_i': 2.8432},
        {'id': 1, 'e_m': 6.208162, 'e_o_k': [3.562060, 2.849648, 2.279719], 'p_i': 20, 'u_i': 4.5844},
        {'id': 2, 'e_m': 2.068426, 'e_o_k': [1.608776, 1.287021], 'p_i': 40, 'u_i': 1.8342},
        {'id': 3, 'e_m': 5.947133, 'e_o_k': [3.412290, 2.729832, 2.183865], 'p_i': 80, 'u_i': 2.1428},
        {'id': 4, 'e_m': 1.464929, 'e_o_k': [0.694750, 0.555800, 0.444640, 0.355712], 'p_i': 10, 'u_i': 3.7337},
        {'id': 5, 'e_m': 0.902234, 'e_o_k': [0.375752, 0.300601, 0.240481, 0.192385, 0.153908], 'p_i': 40, 'u_i': 3.4112},
    ]
    B_BUDGET = 176.640014
    return processors, tasks, B_BUDGET

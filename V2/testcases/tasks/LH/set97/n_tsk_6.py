"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 21, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1097, "set": 97, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.482155, 'e_o_k': [0.200802, 0.160642, 0.128514, 0.102811, 0.082249], 'p_i': 10, 'u_i': 3.2309},
        {'id': 1, 'e_m': 4.321063, 'e_o_k': [1.799586, 1.439669, 1.151735, 0.921388, 0.737110], 'p_i': 20, 'u_i': 2.9440},
        {'id': 2, 'e_m': 0.240290, 'e_o_k': [0.137871, 0.110297, 0.088238], 'p_i': 40, 'u_i': 1.5741},
        {'id': 3, 'e_m': 2.229082, 'e_o_k': [0.845887, 0.676710, 0.541368, 0.433094, 0.346475, 0.277180], 'p_i': 80, 'u_i': 1.4817},
        {'id': 4, 'e_m': 2.063041, 'e_o_k': [1.604588, 1.283670], 'p_i': 40, 'u_i': 3.4660},
        {'id': 5, 'e_m': 1.005690, 'e_o_k': [0.381637, 0.305310, 0.244248, 0.195398, 0.156319, 0.125055], 'p_i': 20, 'u_i': 3.9304},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET

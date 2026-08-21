"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}
"""

_SPEC = '{"B": 88.32, "H": 80, "J": 27, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1017, "set": 17, "sweep": "shape", "util_per_core": 0.2, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.396763, 'e_o_k': [0.092578, 0.092578, 0.092578, 0.092578, 0.092578, 0.092578], 'p_i': 10, 'u_i': 2.9192},
        {'id': 1, 'e_m': 0.524964, 'e_o_k': [0.183737, 0.183737, 0.183737, 0.183737], 'p_i': 20, 'u_i': 2.0454},
        {'id': 2, 'e_m': 3.768792, 'e_o_k': [0.879385, 0.879385, 0.879385, 0.879385, 0.879385, 0.879385], 'p_i': 40, 'u_i': 2.8602},
        {'id': 3, 'e_m': 8.561063, 'e_o_k': [5.992744, 5.992744], 'p_i': 80, 'u_i': 2.9521},
        {'id': 4, 'e_m': 0.427036, 'e_o_k': [0.298925, 0.298925], 'p_i': 10, 'u_i': 3.5497},
        {'id': 5, 'e_m': 1.656317, 'e_o_k': [0.579711, 0.579711, 0.579711, 0.579711], 'p_i': 40, 'u_i': 2.7971},
        {'id': 6, 'e_m': 0.919393, 'e_o_k': [0.214525, 0.214525, 0.214525, 0.214525, 0.214525, 0.214525], 'p_i': 80, 'u_i': 4.6429},
        {'id': 7, 'e_m': 2.979082, 'e_o_k': [2.085357, 2.085357], 'p_i': 80, 'u_i': 1.6248},
    ]
    B_BUDGET = 88.320000
    return processors, tasks, B_BUDGET

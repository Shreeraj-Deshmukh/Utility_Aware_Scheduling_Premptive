"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320009, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320009, "H": 80, "J": 35, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1038, "set": 38, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.070595, 'e_o_k': [0.614276, 0.491421, 0.393137], 'p_i': 10, 'u_i': 2.6411},
        {'id': 1, 'e_m': 1.195922, 'e_o_k': [0.686185, 0.548948, 0.439158], 'p_i': 20, 'u_i': 4.9928},
        {'id': 2, 'e_m': 3.179254, 'e_o_k': [1.824162, 1.459330, 1.167464], 'p_i': 40, 'u_i': 3.9733},
        {'id': 3, 'e_m': 2.010249, 'e_o_k': [1.153422, 0.922737, 0.738190], 'p_i': 80, 'u_i': 1.2745},
        {'id': 4, 'e_m': 0.294507, 'e_o_k': [0.168979, 0.135184, 0.108147], 'p_i': 10, 'u_i': 1.8926},
        {'id': 5, 'e_m': 1.250085, 'e_o_k': [0.717262, 0.573809, 0.459048], 'p_i': 40, 'u_i': 4.4301},
        {'id': 6, 'e_m': 2.310377, 'e_o_k': [1.325626, 1.060501, 0.848401], 'p_i': 40, 'u_i': 2.8023},
        {'id': 7, 'e_m': 0.100727, 'e_o_k': [0.057794, 0.046235, 0.036988], 'p_i': 10, 'u_i': 1.0101},
    ]
    B_BUDGET = 88.320009
    return processors, tasks, B_BUDGET

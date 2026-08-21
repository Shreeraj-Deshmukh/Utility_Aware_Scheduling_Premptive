"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319984, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}
"""

_SPEC = '{"B": 88.319984, "H": 80, "J": 27, "factor": "n_tsk", "n_frq": 8, "n_prc": 2, "n_tsk": 6, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1044, "set": 44, "sweep": "tasks", "util_per_core": 0.2, "value": "6"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.176605, 'e_o_k': [0.101330, 0.081064, 0.064851], 'p_i': 10, 'u_i': 4.9794},
        {'id': 1, 'e_m': 1.736478, 'e_o_k': [0.658955, 0.527164, 0.421731, 0.337385, 0.269908, 0.215926], 'p_i': 20, 'u_i': 1.8563},
        {'id': 2, 'e_m': 1.065864, 'e_o_k': [0.404472, 0.323577, 0.258862, 0.207089, 0.165672, 0.132537], 'p_i': 40, 'u_i': 1.0975},
        {'id': 3, 'e_m': 7.139651, 'e_o_k': [3.386014, 2.708811, 2.167049, 1.733639], 'p_i': 80, 'u_i': 4.1970},
        {'id': 4, 'e_m': 0.460507, 'e_o_k': [0.174752, 0.139802, 0.111841, 0.089473, 0.071578, 0.057263], 'p_i': 10, 'u_i': 1.7417},
        {'id': 5, 'e_m': 2.671454, 'e_o_k': [1.112576, 0.890061, 0.712049, 0.569639, 0.455711], 'p_i': 20, 'u_i': 3.7063},
    ]
    B_BUDGET = 88.319984
    return processors, tasks, B_BUDGET

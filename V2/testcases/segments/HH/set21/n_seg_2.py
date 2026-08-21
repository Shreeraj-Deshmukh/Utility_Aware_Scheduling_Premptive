"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.691442, 'e_o_k': [0.537788, 0.430231], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 3.651177, 'e_o_k': [2.839805, 2.271844], 'p_i': 20, 'u_i': 2.2851},
        {'id': 2, 'e_m': 5.369710, 'e_o_k': [4.176441, 3.341153], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 9.653701, 'e_o_k': [7.508434, 6.006747], 'p_i': 80, 'u_i': 2.3867},
        {'id': 4, 'e_m': 0.756812, 'e_o_k': [0.588632, 0.470906], 'p_i': 10, 'u_i': 1.9527},
        {'id': 5, 'e_m': 0.749641, 'e_o_k': [0.583054, 0.466443], 'p_i': 10, 'u_i': 2.5555},
        {'id': 6, 'e_m': 6.748626, 'e_o_k': [5.248931, 4.199145], 'p_i': 80, 'u_i': 2.5749},
        {'id': 7, 'e_m': 2.335192, 'e_o_k': [1.816260, 1.453008], 'p_i': 40, 'u_i': 4.5972},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET

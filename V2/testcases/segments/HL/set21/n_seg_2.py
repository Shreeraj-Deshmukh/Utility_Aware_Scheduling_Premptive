"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400006, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400006, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1021, "set": 21, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.691442, 'e_o_k': [0.192067, 0.153654], 'p_i': 10, 'u_i': 2.6945},
        {'id': 1, 'e_m': 3.651177, 'e_o_k': [1.014216, 0.811373], 'p_i': 20, 'u_i': 2.2851},
        {'id': 2, 'e_m': 5.369710, 'e_o_k': [1.491586, 1.193269], 'p_i': 40, 'u_i': 1.9156},
        {'id': 3, 'e_m': 9.653701, 'e_o_k': [2.681584, 2.145267], 'p_i': 80, 'u_i': 2.3867},
        {'id': 4, 'e_m': 0.756812, 'e_o_k': [0.210226, 0.168181], 'p_i': 10, 'u_i': 1.9527},
        {'id': 5, 'e_m': 0.749641, 'e_o_k': [0.208233, 0.166587], 'p_i': 10, 'u_i': 2.5555},
        {'id': 6, 'e_m': 6.748626, 'e_o_k': [1.874618, 1.499695], 'p_i': 80, 'u_i': 2.5749},
        {'id': 7, 'e_m': 2.335192, 'e_o_k': [0.648664, 0.518932], 'p_i': 40, 'u_i': 4.5972},
    ]
    B_BUDGET = 110.400006
    return processors, tasks, B_BUDGET

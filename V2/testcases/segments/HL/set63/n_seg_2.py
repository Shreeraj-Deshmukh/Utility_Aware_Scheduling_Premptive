"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.400007, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "segments", "util_per_core": 0.4, "value": "2"}
"""

_SPEC = '{"B": 110.400007, "H": 80, "J": 24, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1063, "set": 63, "sweep": "segments", "util_per_core": 0.4, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.647287, 'e_o_k': [0.457580, 0.366064], 'p_i': 10, 'u_i': 2.3752},
        {'id': 1, 'e_m': 0.034300, 'e_o_k': [0.009528, 0.007622], 'p_i': 20, 'u_i': 4.5040},
        {'id': 2, 'e_m': 2.925892, 'e_o_k': [0.812748, 0.650198], 'p_i': 40, 'u_i': 4.7123},
        {'id': 3, 'e_m': 1.655242, 'e_o_k': [0.459789, 0.367831], 'p_i': 80, 'u_i': 4.3702},
        {'id': 4, 'e_m': 0.978124, 'e_o_k': [0.271701, 0.217361], 'p_i': 20, 'u_i': 3.7678},
        {'id': 5, 'e_m': 1.868312, 'e_o_k': [0.518976, 0.415181], 'p_i': 40, 'u_i': 3.2312},
        {'id': 6, 'e_m': 15.433016, 'e_o_k': [4.286949, 3.429559], 'p_i': 80, 'u_i': 3.7207},
        {'id': 7, 'e_m': 10.047671, 'e_o_k': [2.791020, 2.232816], 'p_i': 40, 'u_i': 2.0745},
    ]
    B_BUDGET = 110.400007
    return processors, tasks, B_BUDGET

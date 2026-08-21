"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 215.279993, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}
"""

_SPEC = '{"B": 215.279993, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1086, "set": 86, "sweep": "util_success", "util_per_core": 0.9, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.399086, 'e_o_k': [0.172019, 0.137615, 0.110092], 'p_i': 10, 'u_i': 2.6742},
        {'id': 1, 'e_m': 0.636977, 'e_o_k': [0.051797, 0.041437, 0.033150, 0.026520, 0.021216, 0.016973], 'p_i': 20, 'u_i': 1.0126},
        {'id': 2, 'e_m': 1.473225, 'e_o_k': [0.131475, 0.105180, 0.084144, 0.067315, 0.053852], 'p_i': 40, 'u_i': 1.6645},
        {'id': 3, 'e_m': 32.835521, 'e_o_k': [2.930348, 2.344278, 1.875422, 1.500338, 1.200270], 'p_i': 80, 'u_i': 1.3774},
        {'id': 4, 'e_m': 8.287391, 'e_o_k': [1.381232, 1.104985], 'p_i': 40, 'u_i': 1.9412},
        {'id': 5, 'e_m': 1.928270, 'e_o_k': [0.321378, 0.257103], 'p_i': 10, 'u_i': 2.2237},
        {'id': 6, 'e_m': 4.286745, 'e_o_k': [0.527059, 0.421647, 0.337318], 'p_i': 10, 'u_i': 2.4269},
        {'id': 7, 'e_m': 28.182525, 'e_o_k': [2.864078, 2.291262, 1.833010, 1.466408], 'p_i': 80, 'u_i': 4.8879},
    ]
    B_BUDGET = 215.279993
    return processors, tasks, B_BUDGET

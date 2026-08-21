"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319998, "H": 80, "J": 30, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "freq", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 88.319998, "H": 80, "J": 30, "factor": "n_frq", "n_frq": 2, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1005, "set": 5, "sweep": "freq", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 1.0]},
        {'id': 1, 'frequencies': [0.4, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.394847, 'e_o_k': [0.187258, 0.149806, 0.119845, 0.095876], 'p_i': 10, 'u_i': 4.2289},
        {'id': 1, 'e_m': 0.122647, 'e_o_k': [0.095392, 0.076314], 'p_i': 20, 'u_i': 3.6434},
        {'id': 2, 'e_m': 1.655397, 'e_o_k': [0.628187, 0.502549, 0.402039, 0.321632, 0.257305, 0.205844], 'p_i': 40, 'u_i': 4.1771},
        {'id': 3, 'e_m': 0.814260, 'e_o_k': [0.386166, 0.308933, 0.247147, 0.197717], 'p_i': 80, 'u_i': 4.0903},
        {'id': 4, 'e_m': 1.025576, 'e_o_k': [0.486384, 0.389107, 0.311286, 0.249029], 'p_i': 20, 'u_i': 2.9627},
        {'id': 5, 'e_m': 0.055175, 'e_o_k': [0.026167, 0.020933, 0.016747, 0.013397], 'p_i': 80, 'u_i': 1.9286},
        {'id': 6, 'e_m': 1.611854, 'e_o_k': [0.764429, 0.611543, 0.489235, 0.391388], 'p_i': 10, 'u_i': 3.5955},
        {'id': 7, 'e_m': 3.586638, 'e_o_k': [1.493721, 1.194977, 0.955982, 0.764785, 0.611828], 'p_i': 40, 'u_i': 1.8182},
    ]
    B_BUDGET = 88.319998
    return processors, tasks, B_BUDGET

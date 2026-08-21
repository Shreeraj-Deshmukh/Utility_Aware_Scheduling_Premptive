"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640009, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.640009, "H": 80, "J": 35, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1060, "set": 60, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.456621, 'e_o_k': [0.937165, 0.562299, 0.337379, 0.202428], 'p_i': 10, 'u_i': 4.9967},
        {'id': 1, 'e_m': 6.472983, 'e_o_k': [4.623559, 2.774135, 1.664481], 'p_i': 20, 'u_i': 3.1686},
        {'id': 2, 'e_m': 1.070031, 'e_o_k': [0.764308, 0.458585, 0.275151], 'p_i': 40, 'u_i': 1.4833},
        {'id': 3, 'e_m': 9.500976, 'e_o_k': [5.580930, 3.348558, 2.009135, 1.205481, 0.723289, 0.433973], 'p_i': 80, 'u_i': 1.9048},
        {'id': 4, 'e_m': 0.365435, 'e_o_k': [0.319756, 0.191854], 'p_i': 40, 'u_i': 4.4078},
        {'id': 5, 'e_m': 0.184044, 'e_o_k': [0.131460, 0.078876, 0.047326], 'p_i': 10, 'u_i': 3.6020},
        {'id': 6, 'e_m': 5.282667, 'e_o_k': [3.398775, 2.039265, 1.223559, 0.734135], 'p_i': 40, 'u_i': 4.8789},
        {'id': 7, 'e_m': 0.255688, 'e_o_k': [0.164505, 0.098703, 0.059222, 0.035533], 'p_i': 10, 'u_i': 3.0372},
    ]
    B_BUDGET = 176.640009
    return processors, tasks, B_BUDGET

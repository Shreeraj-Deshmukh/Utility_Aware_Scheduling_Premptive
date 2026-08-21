"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640017, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "segments", "util_per_core": 0.4, "value": "3"}
"""

_SPEC = '{"B": 176.640017, "H": 80, "J": 37, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1049, "set": 49, "sweep": "segments", "util_per_core": 0.4, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.001859, 'e_o_k': [0.001067, 0.000853, 0.000683], 'p_i': 10, 'u_i': 1.4564},
        {'id': 1, 'e_m': 1.030212, 'e_o_k': [0.591105, 0.472884, 0.378307], 'p_i': 20, 'u_i': 1.4719},
        {'id': 2, 'e_m': 0.499974, 'e_o_k': [0.286870, 0.229496, 0.183597], 'p_i': 40, 'u_i': 1.0831},
        {'id': 3, 'e_m': 3.303812, 'e_o_k': [1.895630, 1.516504, 1.213203], 'p_i': 80, 'u_i': 3.5025},
        {'id': 4, 'e_m': 16.765688, 'e_o_k': [9.619657, 7.695726, 6.156581], 'p_i': 40, 'u_i': 4.4776},
        {'id': 5, 'e_m': 1.698548, 'e_o_k': [0.974577, 0.779662, 0.623729], 'p_i': 20, 'u_i': 3.2024},
        {'id': 6, 'e_m': 0.189483, 'e_o_k': [0.108720, 0.086976, 0.069581], 'p_i': 10, 'u_i': 1.4405},
        {'id': 7, 'e_m': 1.714886, 'e_o_k': [0.983951, 0.787161, 0.629729], 'p_i': 10, 'u_i': 3.4151},
    ]
    B_BUDGET = 176.640017
    return processors, tasks, B_BUDGET

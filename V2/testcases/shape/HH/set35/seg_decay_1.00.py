"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639982, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639982, "H": 80, "J": 33, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1035, "set": 35, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.306627, 'e_o_k': [0.107319, 0.107319, 0.107319, 0.107319], 'p_i': 10, 'u_i': 2.6246},
        {'id': 1, 'e_m': 0.296738, 'e_o_k': [0.069239, 0.069239, 0.069239, 0.069239, 0.069239, 0.069239], 'p_i': 20, 'u_i': 2.3478},
        {'id': 2, 'e_m': 4.540447, 'e_o_k': [2.118875, 2.118875, 2.118875], 'p_i': 40, 'u_i': 2.5491},
        {'id': 3, 'e_m': 14.551355, 'e_o_k': [4.074379, 4.074379, 4.074379, 4.074379, 4.074379], 'p_i': 80, 'u_i': 2.9783},
        {'id': 4, 'e_m': 5.361003, 'e_o_k': [3.752702, 3.752702], 'p_i': 20, 'u_i': 1.6186},
        {'id': 5, 'e_m': 2.936211, 'e_o_k': [0.685116, 0.685116, 0.685116, 0.685116, 0.685116, 0.685116], 'p_i': 40, 'u_i': 2.1935},
        {'id': 6, 'e_m': 1.139762, 'e_o_k': [0.531889, 0.531889, 0.531889], 'p_i': 20, 'u_i': 1.0173},
        {'id': 7, 'e_m': 0.606538, 'e_o_k': [0.424576, 0.424576], 'p_i': 10, 'u_i': 4.7591},
    ]
    B_BUDGET = 176.639982
    return processors, tasks, B_BUDGET

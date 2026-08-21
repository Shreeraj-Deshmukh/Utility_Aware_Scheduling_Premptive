"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.200005, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.200005, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1083, "set": 83, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.786850, 'e_o_k': [0.218570, 0.174856], 'p_i': 10, 'u_i': 3.6650},
        {'id': 1, 'e_m': 0.744352, 'e_o_k': [0.206764, 0.165412], 'p_i': 20, 'u_i': 4.7122},
        {'id': 2, 'e_m': 0.568045, 'e_o_k': [0.157790, 0.126232], 'p_i': 40, 'u_i': 2.7870},
        {'id': 3, 'e_m': 6.876570, 'e_o_k': [1.910158, 1.528127], 'p_i': 80, 'u_i': 1.7506},
        {'id': 4, 'e_m': 2.991189, 'e_o_k': [0.830886, 0.664709], 'p_i': 40, 'u_i': 4.5685},
        {'id': 5, 'e_m': 0.337006, 'e_o_k': [0.093613, 0.074890], 'p_i': 10, 'u_i': 2.7344},
        {'id': 6, 'e_m': 0.443917, 'e_o_k': [0.123310, 0.098648], 'p_i': 40, 'u_i': 1.1398},
        {'id': 7, 'e_m': 5.148870, 'e_o_k': [1.430242, 1.144193], 'p_i': 80, 'u_i': 4.8954},
    ]
    B_BUDGET = 55.200005
    return processors, tasks, B_BUDGET

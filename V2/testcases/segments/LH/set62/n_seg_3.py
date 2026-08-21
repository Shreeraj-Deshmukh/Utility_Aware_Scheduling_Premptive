"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.320002, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 88.320002, "H": 80, "J": 34, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1062, "set": 62, "sweep": "segments", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.059251, 'e_o_k': [0.607767, 0.486214, 0.388971], 'p_i': 10, 'u_i': 2.6711},
        {'id': 1, 'e_m': 0.937251, 'e_o_k': [0.537767, 0.430213, 0.344171], 'p_i': 20, 'u_i': 2.3833},
        {'id': 2, 'e_m': 0.643315, 'e_o_k': [0.369115, 0.295292, 0.236234], 'p_i': 40, 'u_i': 4.1647},
        {'id': 3, 'e_m': 0.856471, 'e_o_k': [0.491418, 0.393134, 0.314507], 'p_i': 80, 'u_i': 1.2796},
        {'id': 4, 'e_m': 1.453835, 'e_o_k': [0.834167, 0.667334, 0.533867], 'p_i': 10, 'u_i': 2.4526},
        {'id': 5, 'e_m': 0.242032, 'e_o_k': [0.138871, 0.111097, 0.088877], 'p_i': 10, 'u_i': 3.7482},
        {'id': 6, 'e_m': 3.782251, 'e_o_k': [2.170144, 1.736115, 1.388892], 'p_i': 80, 'u_i': 2.1247},
        {'id': 7, 'e_m': 0.142351, 'e_o_k': [0.081677, 0.065342, 0.052273], 'p_i': 40, 'u_i': 4.6336},
    ]
    B_BUDGET = 88.320002
    return processors, tasks, B_BUDGET

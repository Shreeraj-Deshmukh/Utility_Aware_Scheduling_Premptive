"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199998, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.199998, "H": 80, "J": 21, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1061, "set": 61, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.342956, 'e_o_k': [0.095266, 0.076213], 'p_i': 10, 'u_i': 3.1491},
        {'id': 1, 'e_m': 1.242204, 'e_o_k': [0.345057, 0.276045], 'p_i': 20, 'u_i': 2.2531},
        {'id': 2, 'e_m': 0.024035, 'e_o_k': [0.006677, 0.005341], 'p_i': 40, 'u_i': 4.0598},
        {'id': 3, 'e_m': 5.660673, 'e_o_k': [1.572409, 1.257927], 'p_i': 80, 'u_i': 4.5014},
        {'id': 4, 'e_m': 4.931490, 'e_o_k': [1.369858, 1.095887], 'p_i': 40, 'u_i': 4.8694},
        {'id': 5, 'e_m': 1.603581, 'e_o_k': [0.445439, 0.356351], 'p_i': 40, 'u_i': 3.6293},
        {'id': 6, 'e_m': 4.803527, 'e_o_k': [1.334313, 1.067450], 'p_i': 80, 'u_i': 4.0966},
        {'id': 7, 'e_m': 0.705118, 'e_o_k': [0.195866, 0.156693], 'p_i': 80, 'u_i': 3.0738},
    ]
    B_BUDGET = 55.199998
    return processors, tasks, B_BUDGET

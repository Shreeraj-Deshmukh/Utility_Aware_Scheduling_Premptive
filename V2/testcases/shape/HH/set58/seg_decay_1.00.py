"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.639955, "H": 80, "J": 40, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}
"""

_SPEC = '{"B": 176.639955, "H": 80, "J": 40, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "shape", "util_per_core": 0.4, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.259080, 'e_o_k': [0.293785, 0.293785, 0.293785, 0.293785, 0.293785, 0.293785], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 3.910652, 'e_o_k': [2.737457, 2.737457], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.555334, 'e_o_k': [0.259156, 0.259156, 0.259156], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 5.117361, 'e_o_k': [3.582153, 3.582153], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 0.830972, 'e_o_k': [0.290840, 0.290840, 0.290840, 0.290840], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 13.997484, 'e_o_k': [9.798239, 9.798239], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 1.327086, 'e_o_k': [0.464480, 0.464480, 0.464480, 0.464480], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.099346, 'e_o_k': [0.034771, 0.034771, 0.034771, 0.034771], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 176.639955
    return processors, tasks, B_BUDGET

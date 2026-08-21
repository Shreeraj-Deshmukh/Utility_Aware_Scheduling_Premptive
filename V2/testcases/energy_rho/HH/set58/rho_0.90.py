"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 166.33598, "H": 80, "J": 40, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.9, "seed": 1058, "set": 58, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.90"}
"""

_SPEC = '{"B": 166.33598, "H": 80, "J": 40, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.9, "seed": 1058, "set": 58, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.90"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.259080, 'e_o_k': [0.477793, 0.382234, 0.305788, 0.244630, 0.195704, 0.156563], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 3.910652, 'e_o_k': [3.041618, 2.433295], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.555334, 'e_o_k': [0.318634, 0.254908, 0.203926], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 5.117361, 'e_o_k': [3.980170, 3.184136], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 0.830972, 'e_o_k': [0.394093, 0.315274, 0.252219, 0.201775], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 13.997484, 'e_o_k': [10.886932, 8.709546], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 1.327086, 'e_o_k': [0.629377, 0.503501, 0.402801, 0.322241], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.099346, 'e_o_k': [0.047115, 0.037692, 0.030154, 0.024123], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 166.335980
    return processors, tasks, B_BUDGET

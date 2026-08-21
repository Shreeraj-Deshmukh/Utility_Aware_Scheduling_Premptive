"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640003, "H": 80, "J": 40, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}
"""

_SPEC = '{"B": 176.640003, "H": 80, "J": 40, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "shape", "util_per_core": 0.4, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.259080, 'e_o_k': [0.739591, 0.443755, 0.266253, 0.159752, 0.095851, 0.057511], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 3.910652, 'e_o_k': [3.421821, 2.053092], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.555334, 'e_o_k': [0.396667, 0.238000, 0.142800], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 5.117361, 'e_o_k': [4.477691, 2.686615], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 0.830972, 'e_o_k': [0.534633, 0.320780, 0.192468, 0.115481], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 13.997484, 'e_o_k': [12.247799, 7.348679], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 1.327086, 'e_o_k': [0.853824, 0.512294, 0.307376, 0.184426], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.099346, 'e_o_k': [0.063918, 0.038351, 0.023010, 0.013806], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 176.640003
    return processors, tasks, B_BUDGET

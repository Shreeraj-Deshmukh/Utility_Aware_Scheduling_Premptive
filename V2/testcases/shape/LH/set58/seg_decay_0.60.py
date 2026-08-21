"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.319983, "H": 80, "J": 40, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}
"""

_SPEC = '{"B": 88.319983, "H": 80, "J": 40, "factor": "seg_decay", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1058, "set": 58, "sweep": "shape", "util_per_core": 0.2, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.629540, 'e_o_k': [0.369796, 0.221877, 0.133126, 0.079876, 0.047926, 0.028755], 'p_i': 10, 'u_i': 4.1820},
        {'id': 1, 'e_m': 1.955326, 'e_o_k': [1.710910, 1.026546], 'p_i': 20, 'u_i': 2.8729},
        {'id': 2, 'e_m': 0.277667, 'e_o_k': [0.198334, 0.119000, 0.071400], 'p_i': 40, 'u_i': 4.4646},
        {'id': 3, 'e_m': 2.558681, 'e_o_k': [2.238846, 1.343307], 'p_i': 80, 'u_i': 2.8456},
        {'id': 4, 'e_m': 0.415486, 'e_o_k': [0.267316, 0.160390, 0.096234, 0.057740], 'p_i': 10, 'u_i': 4.6357},
        {'id': 5, 'e_m': 6.998742, 'e_o_k': [6.123899, 3.674340], 'p_i': 80, 'u_i': 3.1275},
        {'id': 6, 'e_m': 0.663543, 'e_o_k': [0.426912, 0.256147, 0.153688, 0.092213], 'p_i': 10, 'u_i': 2.7677},
        {'id': 7, 'e_m': 0.049673, 'e_o_k': [0.031959, 0.019175, 0.011505, 0.006903], 'p_i': 10, 'u_i': 2.2237},
    ]
    B_BUDGET = 88.319983
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 104.512007, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.3, "seed": 1004, "set": 4, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.30"}
"""

_SPEC = '{"B": 104.512007, "H": 80, "J": 33, "factor": "rho", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 0.3, "seed": 1004, "set": 4, "sweep": "energy_rho", "util_per_core": 0.4, "value": "0.30"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.929756, 'e_o_k': [0.352822, 0.282257, 0.225806, 0.180645, 0.144516, 0.115613], 'p_i': 10, 'u_i': 2.4783},
        {'id': 1, 'e_m': 0.056878, 'e_o_k': [0.021584, 0.017267, 0.013814, 0.011051, 0.008841, 0.007073], 'p_i': 20, 'u_i': 1.9438},
        {'id': 2, 'e_m': 2.623994, 'e_o_k': [2.040884, 1.632707], 'p_i': 40, 'u_i': 1.5728},
        {'id': 3, 'e_m': 4.474673, 'e_o_k': [3.480301, 2.784241], 'p_i': 80, 'u_i': 1.5110},
        {'id': 4, 'e_m': 2.349668, 'e_o_k': [1.827520, 1.462016], 'p_i': 20, 'u_i': 4.3454},
        {'id': 5, 'e_m': 10.542988, 'e_o_k': [5.000062, 4.000050, 3.200040, 2.560032], 'p_i': 40, 'u_i': 2.7253},
        {'id': 6, 'e_m': 0.342456, 'e_o_k': [0.266355, 0.213084], 'p_i': 10, 'u_i': 1.4714},
        {'id': 7, 'e_m': 3.346871, 'e_o_k': [2.603122, 2.082497], 'p_i': 20, 'u_i': 2.9160},
    ]
    B_BUDGET = 104.512007
    return processors, tasks, B_BUDGET

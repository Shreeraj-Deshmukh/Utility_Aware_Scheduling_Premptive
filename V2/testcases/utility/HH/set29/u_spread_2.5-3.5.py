"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640002, "H": 80, "J": 28, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 176.640002, "H": 80, "J": 28, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1029, "set": 29, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.555176, 'e_o_k': [0.263295, 0.210636, 0.168509, 0.134807], 'p_i': 10, 'u_i': 2.8688},
        {'id': 1, 'e_m': 0.851460, 'e_o_k': [0.354606, 0.283685, 0.226948, 0.181558, 0.145247], 'p_i': 20, 'u_i': 3.1661},
        {'id': 2, 'e_m': 3.395703, 'e_o_k': [1.414203, 1.131362, 0.905090, 0.724072, 0.579257], 'p_i': 40, 'u_i': 2.8244},
        {'id': 3, 'e_m': 3.482314, 'e_o_k': [1.450273, 1.160219, 0.928175, 0.742540, 0.594032], 'p_i': 80, 'u_i': 3.4660},
        {'id': 4, 'e_m': 4.033383, 'e_o_k': [3.137075, 2.509660], 'p_i': 40, 'u_i': 3.3761},
        {'id': 5, 'e_m': 2.789347, 'e_o_k': [1.600445, 1.280356, 1.024285], 'p_i': 80, 'u_i': 2.5005},
        {'id': 6, 'e_m': 3.567276, 'e_o_k': [1.691798, 1.353438, 1.082751, 0.866200], 'p_i': 40, 'u_i': 3.4882},
        {'id': 7, 'e_m': 3.486046, 'e_o_k': [2.711369, 2.169095], 'p_i': 10, 'u_i': 2.8397},
    ]
    B_BUDGET = 176.640002
    return processors, tasks, B_BUDGET

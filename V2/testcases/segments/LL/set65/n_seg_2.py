"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.2, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.2, "value": "2"}
"""

_SPEC = '{"B": 55.2, "H": 80, "J": 28, "factor": "n_seg", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "segments", "util_per_core": 0.2, "value": "2"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.063904, 'e_o_k': [0.017751, 0.014201], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 2.319143, 'e_o_k': [0.644207, 0.515365], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.400395, 'e_o_k': [0.111221, 0.088977], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 4.718930, 'e_o_k': [1.310814, 1.048651], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 1.741564, 'e_o_k': [0.483768, 0.387014], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 7.261818, 'e_o_k': [2.017172, 1.613737], 'p_i': 80, 'u_i': 4.6158},
        {'id': 6, 'e_m': 0.036678, 'e_o_k': [0.010188, 0.008151], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 0.579422, 'e_o_k': [0.160951, 0.128760], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 55.200000
    return processors, tasks, B_BUDGET

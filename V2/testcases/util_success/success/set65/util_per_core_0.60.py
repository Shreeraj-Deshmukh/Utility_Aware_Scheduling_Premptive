"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.519986, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.519986, "H": 80, "J": 28, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.191711, 'e_o_k': [0.019483, 0.015586, 0.012469, 0.009975], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 6.957430, 'e_o_k': [0.855422, 0.684337, 0.547470], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 1.201185, 'e_o_k': [0.147687, 0.118149, 0.094519], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 14.156791, 'e_o_k': [1.740589, 1.392471, 1.113977], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 5.224693, 'e_o_k': [0.530965, 0.424772, 0.339817, 0.271854], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 21.785455, 'e_o_k': [1.771521, 1.417217, 1.133773, 0.907019, 0.725615, 0.580492], 'p_i': 80, 'u_i': 1.3665},
        {'id': 6, 'e_m': 0.110033, 'e_o_k': [0.011182, 0.008946, 0.007157, 0.005725], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 1.738266, 'e_o_k': [0.155128, 0.124103, 0.099282, 0.079426, 0.063541], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 143.519986
    return processors, tasks, B_BUDGET

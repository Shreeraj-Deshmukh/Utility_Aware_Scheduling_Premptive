"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 55.199986, "H": 80, "J": 28, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "freq", "util_per_core": 0.2, "value": "3"}
"""

_SPEC = '{"B": 55.199986, "H": 80, "J": 28, "factor": "n_frq", "n_frq": 3, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "LL", "rho": 1.0, "seed": 1065, "set": 65, "sweep": "freq", "util_per_core": 0.2, "value": "3"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.4, 0.7, 1.0]},
        {'id': 1, 'frequencies': [0.4, 0.7, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.063904, 'e_o_k': [0.010824, 0.008659, 0.006927, 0.005542], 'p_i': 10, 'u_i': 3.7146},
        {'id': 1, 'e_m': 2.319143, 'e_o_k': [0.475234, 0.380187, 0.304150], 'p_i': 20, 'u_i': 2.7971},
        {'id': 2, 'e_m': 0.400395, 'e_o_k': [0.082048, 0.065639, 0.052511], 'p_i': 40, 'u_i': 1.6396},
        {'id': 3, 'e_m': 4.718930, 'e_o_k': [0.966994, 0.773595, 0.618876], 'p_i': 80, 'u_i': 4.1445},
        {'id': 4, 'e_m': 1.741564, 'e_o_k': [0.294980, 0.235984, 0.188787, 0.151030], 'p_i': 20, 'u_i': 4.6205},
        {'id': 5, 'e_m': 7.261818, 'e_o_k': [0.984178, 0.787343, 0.629874, 0.503899, 0.403119, 0.322496], 'p_i': 80, 'u_i': 1.3665},
        {'id': 6, 'e_m': 0.036678, 'e_o_k': [0.006212, 0.004970, 0.003976, 0.003181], 'p_i': 20, 'u_i': 3.3652},
        {'id': 7, 'e_m': 0.579422, 'e_o_k': [0.086182, 0.068946, 0.055157, 0.044125, 0.035300], 'p_i': 20, 'u_i': 2.1692},
    ]
    B_BUDGET = 55.199986
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 176.640007, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 176.640007, "H": 80, "J": 33, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "HH", "rho": 1.0, "seed": 1009, "set": 9, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 1.737228, 'e_o_k': [1.351177, 1.080942], 'p_i': 10, 'u_i': 2.7033},
        {'id': 1, 'e_m': 1.414064, 'e_o_k': [0.536606, 0.429285, 0.343428, 0.274742, 0.219794, 0.175835], 'p_i': 20, 'u_i': 2.5779},
        {'id': 2, 'e_m': 8.894962, 'e_o_k': [3.704470, 2.963576, 2.370861, 1.896689, 1.517351], 'p_i': 40, 'u_i': 2.6608},
        {'id': 3, 'e_m': 3.992321, 'e_o_k': [3.105138, 2.484111], 'p_i': 80, 'u_i': 3.0707},
        {'id': 4, 'e_m': 0.156022, 'e_o_k': [0.064978, 0.051982, 0.041586, 0.033269, 0.026615], 'p_i': 20, 'u_i': 2.5149},
        {'id': 5, 'e_m': 0.352177, 'e_o_k': [0.202069, 0.161655, 0.129324], 'p_i': 20, 'u_i': 3.3649},
        {'id': 6, 'e_m': 5.127088, 'e_o_k': [2.431546, 1.945237, 1.556189, 1.244951], 'p_i': 40, 'u_i': 3.4706},
        {'id': 7, 'e_m': 1.297088, 'e_o_k': [0.744231, 0.595385, 0.476308], 'p_i': 10, 'u_i': 2.6402},
    ]
    B_BUDGET = 176.640007
    return processors, tasks, B_BUDGET

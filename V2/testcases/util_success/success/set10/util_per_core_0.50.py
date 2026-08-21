"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.600015, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.600015, "H": 80, "J": 31, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1010, "set": 10, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.554030, 'e_o_k': [0.045052, 0.036041, 0.028833, 0.023067, 0.018453, 0.014763], 'p_i': 10, 'u_i': 3.7777},
        {'id': 1, 'e_m': 0.481296, 'e_o_k': [0.042952, 0.034362, 0.027490, 0.021992, 0.017593], 'p_i': 20, 'u_i': 2.9102},
        {'id': 2, 'e_m': 8.983690, 'e_o_k': [0.912977, 0.730381, 0.584305, 0.467444], 'p_i': 40, 'u_i': 3.0744},
        {'id': 3, 'e_m': 25.775890, 'e_o_k': [4.295982, 3.436785], 'p_i': 80, 'u_i': 3.1102},
        {'id': 4, 'e_m': 1.814425, 'e_o_k': [0.147543, 0.118034, 0.094428, 0.075542, 0.060434, 0.048347], 'p_i': 20, 'u_i': 3.9746},
        {'id': 5, 'e_m': 1.682875, 'e_o_k': [0.206911, 0.165529, 0.132423], 'p_i': 10, 'u_i': 1.5757},
        {'id': 6, 'e_m': 2.584921, 'e_o_k': [0.317818, 0.254255, 0.203404], 'p_i': 40, 'u_i': 4.9941},
        {'id': 7, 'e_m': 2.004384, 'e_o_k': [0.334064, 0.267251], 'p_i': 40, 'u_i': 1.7632},
    ]
    B_BUDGET = 119.600015
    return processors, tasks, B_BUDGET

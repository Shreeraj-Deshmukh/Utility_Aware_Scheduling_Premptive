"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 119.599994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}
"""

_SPEC = '{"B": 119.599994, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.5, "value": "0.50"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.288049, 'e_o_k': [0.023423, 0.018739, 0.014991, 0.011993, 0.009594, 0.007675], 'p_i': 10, 'u_i': 2.8095},
        {'id': 1, 'e_m': 2.150880, 'e_o_k': [0.264452, 0.211562, 0.169250], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 5.933946, 'e_o_k': [0.529564, 0.423652, 0.338921, 0.271137, 0.216910], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 6.861241, 'e_o_k': [0.843595, 0.674876, 0.539901], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 3.284919, 'e_o_k': [0.293157, 0.234525, 0.187620, 0.150096, 0.120077], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 2.533506, 'e_o_k': [0.226098, 0.180879, 0.144703, 0.115762, 0.092610], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 15.407046, 'e_o_k': [1.374974, 1.099979, 0.879984, 0.703987, 0.563189], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 1.548181, 'e_o_k': [0.190350, 0.152280, 0.121824], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 119.599994
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 95.680006, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}
"""

_SPEC = '{"B": 95.680006, "H": 80, "J": 29, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1072, "set": 72, "sweep": "util_success", "util_per_core": 0.4, "value": "0.40"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.230439, 'e_o_k': [0.018739, 0.014991, 0.011993, 0.009594, 0.007675, 0.006140], 'p_i': 10, 'u_i': 2.8095},
        {'id': 1, 'e_m': 1.720704, 'e_o_k': [0.211562, 0.169250, 0.135400], 'p_i': 20, 'u_i': 2.2645},
        {'id': 2, 'e_m': 4.747157, 'e_o_k': [0.423652, 0.338921, 0.271137, 0.216910, 0.173528], 'p_i': 40, 'u_i': 4.9290},
        {'id': 3, 'e_m': 5.488993, 'e_o_k': [0.674876, 0.539901, 0.431921], 'p_i': 80, 'u_i': 2.8289},
        {'id': 4, 'e_m': 2.627935, 'e_o_k': [0.234525, 0.187620, 0.150096, 0.120077, 0.096062], 'p_i': 20, 'u_i': 2.4039},
        {'id': 5, 'e_m': 2.026805, 'e_o_k': [0.180879, 0.144703, 0.115762, 0.092610, 0.074088], 'p_i': 10, 'u_i': 2.7593},
        {'id': 6, 'e_m': 12.325637, 'e_o_k': [1.099979, 0.879984, 0.703987, 0.563189, 0.450552], 'p_i': 80, 'u_i': 4.9185},
        {'id': 7, 'e_m': 1.238545, 'e_o_k': [0.152280, 0.121824, 0.097459], 'p_i': 80, 'u_i': 1.9966},
    ]
    B_BUDGET = 95.680006
    return processors, tasks, B_BUDGET

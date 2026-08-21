"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 239.199992, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}
"""

_SPEC = '{"B": 239.199992, "H": 80, "J": 34, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1039, "set": 39, "sweep": "util_success", "util_per_core": 1.0, "value": "1.00"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 4.589595, 'e_o_k': [0.466422, 0.373138, 0.298510, 0.238808], 'p_i': 10, 'u_i': 2.7515},
        {'id': 1, 'e_m': 7.896446, 'e_o_k': [1.316074, 1.052860], 'p_i': 20, 'u_i': 4.8495},
        {'id': 2, 'e_m': 14.641870, 'e_o_k': [1.487995, 1.190396, 0.952317, 0.761853], 'p_i': 40, 'u_i': 3.9350},
        {'id': 3, 'e_m': 26.444500, 'e_o_k': [4.407417, 3.525933], 'p_i': 80, 'u_i': 4.4741},
        {'id': 4, 'e_m': 5.018627, 'e_o_k': [0.836438, 0.669150], 'p_i': 40, 'u_i': 1.8290},
        {'id': 5, 'e_m': 2.718164, 'e_o_k': [0.453027, 0.362422], 'p_i': 10, 'u_i': 3.8600},
        {'id': 6, 'e_m': 2.018532, 'e_o_k': [0.248180, 0.198544, 0.158835], 'p_i': 80, 'u_i': 4.0344},
        {'id': 7, 'e_m': 0.271015, 'e_o_k': [0.045169, 0.036135], 'p_i': 10, 'u_i': 3.0439},
    ]
    B_BUDGET = 239.199992
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 110.40002, "H": 80, "J": 21, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}
"""

_SPEC = '{"B": 110.40002, "H": 80, "J": 21, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.5, "periods": [10, 20, 40, 80], "regime": "HL", "rho": 1.0, "seed": 1019, "set": 19, "sweep": "utility", "util_per_core": 0.4, "value": "2.5-3.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 3.059421, 'e_o_k': [0.518195, 0.414556, 0.331645, 0.265316], 'p_i': 10, 'u_i': 2.7254},
        {'id': 1, 'e_m': 2.238024, 'e_o_k': [0.621673, 0.497339], 'p_i': 20, 'u_i': 3.2751},
        {'id': 2, 'e_m': 0.750637, 'e_o_k': [0.127140, 0.101712, 0.081370, 0.065096], 'p_i': 40, 'u_i': 2.9090},
        {'id': 3, 'e_m': 5.306501, 'e_o_k': [1.087398, 0.869918, 0.695935], 'p_i': 80, 'u_i': 3.3394},
        {'id': 4, 'e_m': 0.055926, 'e_o_k': [0.009473, 0.007578, 0.006062, 0.004850], 'p_i': 40, 'u_i': 3.3096},
        {'id': 5, 'e_m': 0.091009, 'e_o_k': [0.013537, 0.010829, 0.008663, 0.006931, 0.005545], 'p_i': 80, 'u_i': 2.5439},
        {'id': 6, 'e_m': 18.185686, 'e_o_k': [5.051579, 4.041264], 'p_i': 80, 'u_i': 2.9942},
        {'id': 7, 'e_m': 2.688109, 'e_o_k': [0.364313, 0.291451, 0.233161, 0.186528, 0.149223, 0.119378], 'p_i': 40, 'u_i': 3.4699},
    ]
    B_BUDGET = 110.400020
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 143.520013, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}
"""

_SPEC = '{"B": 143.520013, "H": 80, "J": 24, "factor": "util_per_core", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 0.3, "periods": [10, 20, 40, 80], "regime": "success", "rho": 1.0, "seed": 1008, "set": 8, "sweep": "util_success", "util_per_core": 0.6, "value": "0.60"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.321021, 'e_o_k': [0.039470, 0.031576, 0.025261], 'p_i': 10, 'u_i': 3.1459},
        {'id': 1, 'e_m': 0.520643, 'e_o_k': [0.064014, 0.051211, 0.040969], 'p_i': 20, 'u_i': 1.5731},
        {'id': 2, 'e_m': 4.556165, 'e_o_k': [0.759361, 0.607489], 'p_i': 40, 'u_i': 4.9538},
        {'id': 3, 'e_m': 34.594159, 'e_o_k': [3.087294, 2.469835, 1.975868, 1.580695, 1.264556], 'p_i': 80, 'u_i': 2.3994},
        {'id': 4, 'e_m': 7.117655, 'e_o_k': [1.186276, 0.949021], 'p_i': 40, 'u_i': 1.5904},
        {'id': 5, 'e_m': 14.922013, 'e_o_k': [1.834674, 1.467739, 1.174191], 'p_i': 40, 'u_i': 2.4893},
        {'id': 6, 'e_m': 0.186212, 'e_o_k': [0.022895, 0.018316, 0.014653], 'p_i': 20, 'u_i': 4.7173},
        {'id': 7, 'e_m': 2.818585, 'e_o_k': [0.469764, 0.375811], 'p_i': 80, 'u_i': 2.7558},
    ]
    B_BUDGET = 143.520013
    return processors, tasks, B_BUDGET

"""Auto-generated USRT testcase -- DO NOT EDIT BY HAND.

Provenance (regenerate from usrt.gen with this spec + seed):
{"B": 88.32002, "H": 80, "J": 34, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}
"""

_SPEC = '{"B": 88.32002, "H": 80, "J": 34, "factor": "u_spread", "n_frq": 8, "n_prc": 2, "n_tsk": 8, "opt_ratio": 1.4, "periods": [10, 20, 40, 80], "regime": "LH", "rho": 1.0, "seed": 1092, "set": 92, "sweep": "utility", "util_per_core": 0.2, "value": "1.5-4.5"}'


def testcase():
    processors = [
        {'id': 0, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
        {'id': 1, 'frequencies': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]},
    ]
    tasks = [
        {'id': 0, 'e_m': 0.279536, 'e_o_k': [0.116418, 0.093134, 0.074507, 0.059606, 0.047685], 'p_i': 10, 'u_i': 3.5552},
        {'id': 1, 'e_m': 0.807491, 'e_o_k': [0.306425, 0.245140, 0.196112, 0.156890, 0.125512, 0.100409], 'p_i': 20, 'u_i': 1.6216},
        {'id': 2, 'e_m': 3.179023, 'e_o_k': [1.824029, 1.459224, 1.167379], 'p_i': 40, 'u_i': 3.8814},
        {'id': 3, 'e_m': 7.775197, 'e_o_k': [3.687424, 2.949939, 2.359951, 1.887961], 'p_i': 80, 'u_i': 2.2065},
        {'id': 4, 'e_m': 0.001832, 'e_o_k': [0.001425, 0.001140], 'p_i': 10, 'u_i': 2.6320},
        {'id': 5, 'e_m': 1.937647, 'e_o_k': [1.111765, 0.889412, 0.711529], 'p_i': 80, 'u_i': 3.4883},
        {'id': 6, 'e_m': 0.361320, 'e_o_k': [0.171358, 0.137086, 0.109669, 0.087735], 'p_i': 10, 'u_i': 3.1487},
        {'id': 7, 'e_m': 3.778825, 'e_o_k': [1.792126, 1.433700, 1.146960, 0.917568], 'p_i': 40, 'u_i': 4.0220},
    ]
    B_BUDGET = 88.320020
    return processors, tasks, B_BUDGET
